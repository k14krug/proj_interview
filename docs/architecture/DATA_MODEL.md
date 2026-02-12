# DATA_MODEL.md
Project: K2 Daily Brief

## 1. Scope and Intent (Phase 1 / V1)

This document defines the **Phase 1 (V1)** data model only.

- V1 supports RSS ingestion, Event Cluster formation, human selection, AI article generation, and Daily Brief compilation.
- Phase 2 (“clean daily reader” refinements such as automated generation, story evolution, delta updates) is intentionally excluded.

Terminology:
- **Internal (DB/code):** `clusters` = *Event Clusters*
- **UI (reader-facing later):** *Events*
- **Raw RSS items:** *Source Articles*
- **AI output:** *Articles*
- **Collections:** *Daily Briefs*

---

## 2. Design Principles

1. All timestamps stored in **UTC** (`DATETIME`), displayed in local time in the app.
2. **Generated content is immutable after finalization** (content fields are not updated after `success`; lifecycle status fields may transition to terminal state).
3. **Raw feed data is immutable** after insert.
4. Clear lineage: **Source Article → Event Cluster → Generated Article → Daily Brief**.
5. Multi-user isolation enforced at query layer (always filter by `user_id` where applicable).
6. MySQL 8.x only at `127.0.0.1:3306` (utf8mb4).

---

## 3. Core Entities

### 3.1 users

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| email | VARCHAR(255) | Unique |
| password_hash | VARCHAR(255) | |
| created_at | DATETIME (UTC) | |
| activated_at | DATETIME (UTC) | Nullable; set on first successful login/activation |
| last_login_at | DATETIME (UTC) | Nullable |
| is_active | BOOLEAN | Default true; may be false for pending/cached users |

Indexes/constraints:
- Unique: `email`

Lifecycle notes:
- V1 may support a pending/cached registration state (see `FR-001C`) by setting `is_active=false` at creation time.
- Pending users are considered expired if not activated within 48 hours of `created_at`.

---

### 3.2 user_preferences

One row per user.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| user_id | FK → users.id | Unique (1:1) |
| topics_json | JSON | Optional |
| source_whitelist_json | JSON | Optional |
| source_blacklist_json | JSON | Optional |
| timezone | VARCHAR(64) | Display timezone; default PDT if unset (e.g., America/Los_Angeles) |

Indexes/constraints:
- Unique: `user_id`

---

### 3.3 rss_sources

Global feed registry.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| name | VARCHAR(255) | |
| base_url | VARCHAR(512) | Optional |
| rss_url | VARCHAR(1024) | Unique (required) |
| is_active | BOOLEAN | Default true |
| created_at | DATETIME (UTC) | |

Indexes/constraints:
- Unique: `rss_url`

---

### 3.4 raw_articles  (Source Articles)

RSS-ingested items. Immutable after insert.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| rss_source_id | FK → rss_sources.id | |
| title | TEXT | |
| summary | TEXT | Nullable |
| url | VARCHAR(2048) | Unique |
| published_at | DATETIME (UTC) | Nullable |
| fetched_at | DATETIME (UTC) | |
| content_hash | VARCHAR(64) | Fallback dedupe |
| full_text | LONGTEXT | Nullable; extracted readable text when available |
| full_text_fetched_at | DATETIME (UTC) | Nullable |
| full_text_status | ENUM('not_attempted','fetched','blocked','error') | Default not_attempted |
| embedding_vector | BLOB | Nullable |
| embedding_model | VARCHAR(128) | Nullable |

Indexes/constraints:
- Unique: `url`
- Index: `published_at`
- Index: `rss_source_id`
- Index: `content_hash` (optional)

Retention:
- Purge allowed by admin policy only for rows not referenced by `generated_article_sources` (see V1 requirements document).

---

### 3.5 clusters  (Event Clusters)

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| first_seen_at | DATETIME (UTC) | |
| last_updated_at | DATETIME (UTC) | |
| article_count | INT | Cached |
| status | ENUM('new','reviewed') | Workflow only (not generation-coupled) |
| info_gap_label | ENUM('thin','moderate','high_depth') | Cached indicator for UI |
| info_gap_score | DECIMAL(5,2) | Optional cached score used to derive label |
| info_gap_evaluated_at | DATETIME (UTC) | Nullable |
| is_closed | BOOLEAN | Default false |
| closed_at | DATETIME (UTC) | Nullable |

Indexes:
- Index: `last_updated_at`
- Index: `status`
- Index: `info_gap_label`

Notes:
- Clusters are global entities in V1.
- User-specific source preferences are enforced in query/service filtering when presenting cluster content.

---

### 3.6 cluster_articles

Join between `raw_articles` and `clusters`.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| cluster_id | FK → clusters.id | |
| raw_article_id | FK → raw_articles.id | |
| added_at | DATETIME (UTC) | |

Indexes/constraints:
- Unique composite: (`cluster_id`, `raw_article_id`)
- Index: `cluster_id`
- Index: `raw_article_id`

---

### 3.7 generated_articles  (Content immutable after finalization)

AI-created article records with async lifecycle status.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| user_id | FK → users.id | |
| cluster_id | FK → clusters.id | |
| headline | VARCHAR(512) | |
| body | LONGTEXT | |
| summary_bullet | TEXT | |
| created_at | DATETIME (UTC) | |
| prompt_snapshot | LONGTEXT | Exact prompt |
| response_snapshot | LONGTEXT | Exact model response |
| model_used | VARCHAR(128) | |
| generation_status | ENUM('queued','running','success','failed') | |
| generation_started_at | DATETIME (UTC) | Nullable |
| generation_finished_at | DATETIME (UTC) | Nullable |
| error_message | TEXT | Nullable |
| latency_ms | INT | Nullable |
| input_tokens | INT | Nullable |
| output_tokens | INT | Nullable |
| total_tokens | INT | Nullable |
| request_id | VARCHAR(128) | Nullable (provider request id) |

Indexes:
- Index: `user_id`
- Index: `cluster_id`
- Index: `created_at`
- Index: `generation_status`
- Unique composite: (`id`, `user_id`) (supports same-user FK checks from join tables)

---

### 3.8 generated_article_sources

Lineage: which raw articles were used.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| generated_article_id | FK → generated_articles.id | |
| raw_article_id | FK → raw_articles.id | |

Indexes/constraints:
- Unique composite: (`generated_article_id`, `raw_article_id`)
- Index: `generated_article_id`
- Index: `raw_article_id`
- FK policy: `raw_article_id` should use `ON DELETE RESTRICT` to preserve lineage for immutable generated content

---

### 3.8A generated_article_citations  (V1-lite audit provenance)

Per-citation provenance map for Synthesis Audit.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| generated_article_id | FK → generated_articles.id | |
| citation_label | VARCHAR(32) | e.g., `[1]` |
| raw_article_id | FK → raw_articles.id | |
| excerpt_text | TEXT | Nullable; supporting snippet when available |
| provenance_status | ENUM('verified_excerpt','source_only','unverified') | |
| excerpt_char_start | INT | Nullable; reserved for future exact highlighting |
| excerpt_char_end | INT | Nullable; reserved for future exact highlighting |
| created_at | DATETIME (UTC) | |

Indexes/constraints:
- Unique composite: (`generated_article_id`, `citation_label`)
- Index: `generated_article_id`
- Index: `raw_article_id`
- Index: `provenance_status`
- FK policy: `raw_article_id` should use `ON DELETE RESTRICT` to preserve audit provenance for immutable generated content

---

### 3.9 briefings  (Daily Briefs; immutable)

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| user_id | FK → users.id | |
| title | VARCHAR(255) | Optional |
| created_at | DATETIME (UTC) | |

Indexes:
- Index: `user_id`
- Index: `created_at`
- Unique composite: (`id`, `user_id`) (supports same-user FK checks from join tables)

---

### 3.10 briefing_articles

Join between `briefings` and `generated_articles`, ordered.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| briefing_id | FK → briefings.id | |
| generated_article_id | FK → generated_articles.id | |
| user_id | FK → users.id | Denormalized for DB-enforced same-user integrity |
| position | INT | 1..N |

Indexes/constraints:
- Unique composite: (`briefing_id`, `generated_article_id`)
- Unique composite: (`briefing_id`, `position`)
- Index: `user_id`
- Composite FK: (`briefing_id`, `user_id`) → `briefings(id, user_id)`
- Composite FK: (`generated_article_id`, `user_id`) → `generated_articles(id, user_id)`
- Index: `briefing_id`

---

### 3.11 job_runs

Operational scheduler ledger for at-most-once execution per schedule slot.

| Field | Type | Notes |
|------|------|------|
| id | PK | |
| job_name | VARCHAR(128) | e.g., rss_ingestion |
| scheduled_for | DATETIME (UTC) | Canonical schedule slot timestamp |
| started_at | DATETIME (UTC) | |
| finished_at | DATETIME (UTC) | Nullable |
| status | ENUM('running','success','failed','skipped_timeout') | |
| worker_instance | VARCHAR(128) | Optional process/host id |
| error_message | TEXT | Nullable |

Indexes/constraints:
- Unique composite: (`job_name`, `scheduled_for`)
- Index: `status`
- Index: `started_at`

---

## 4. Relationship Summary (Corrected)

- `users` 1:1 `user_preferences`
- `users` 1:M `generated_articles`
- `users` 1:M `briefings`
- `rss_sources` 1:M `raw_articles`
- `clusters` M:N `raw_articles` via `cluster_articles`
- `clusters` 1:M `generated_articles`
- `generated_articles` M:N `raw_articles` via `generated_article_sources`
- `generated_articles` 1:M `generated_article_citations`
- `briefings` M:N `generated_articles` via `briefing_articles` (same-user join enforced by composite FKs)

---

## 5. Data Flow (V1)

1. RSS ingestion inserts → `raw_articles`
2. Similarity logic assigns → `cluster_articles` (+ updates `clusters.last_updated_at`, `article_count`)
3. Information Gap indicator is computed and cached on `clusters` (`info_gap_label`, optional `info_gap_score`)
4. User selects source articles in an Event Cluster
5. Generate action creates `generated_articles` row with `generation_status='queued'`
6. Worker processes generation (`running` → `success`/`failed`) and stores prompt+response+metadata
7. Lineage recorded → `generated_article_sources` (on successful generation)
8. Citation provenance recorded → `generated_article_citations` (source link required; excerpt optional in V1)
9. User compiles a Daily Brief → `briefings` + `briefing_articles` (same `user_id` required)

---

## 6. Indexing Notes

High-impact indexes for V1:

- `raw_articles.url` (unique)
- `raw_articles.published_at`
- `cluster_articles.cluster_id`
- `cluster_articles.raw_article_id`
- `clusters.last_updated_at`
- `clusters.info_gap_label`
- `generated_articles.user_id`
- `briefings.user_id`
- `briefing_articles.briefing_id`
- `job_runs(job_name, scheduled_for)` (unique)
- `generated_article_citations.generated_article_id`

---

## 7. Deletion / Retention Policy (V1)

Append-only (no deletes in normal operation):
- generated_articles
- generated_article_sources
- generated_article_citations
- briefings
- briefing_articles

Admin purge allowed:
- raw_articles (including full_text/embeddings) after a retention window only when not referenced by `generated_article_sources` or `generated_article_citations`
- clusters/cluster_articles only if not referenced by generated_articles

Recommended purge pattern:
- Use `NOT EXISTS` against both `generated_article_sources` and `generated_article_citations` when deleting `raw_articles`.

---

## 8. Future Extension Points (Not V1)

- cluster_versions (story evolution snapshots)
- automated generation flags / schedules
- per-user event subscriptions and notifications
- source scoring and credibility metadata
- richer entity extraction for clustering
- exact character/span highlight rendering in Synthesis Audit using `excerpt_char_start`/`excerpt_char_end`
