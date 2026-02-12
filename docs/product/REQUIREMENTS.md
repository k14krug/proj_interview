# REQUIREMENTS.md
Project Name: K2 Daily Brief

## 1. Version Scope

This document defines **Phase 1 (V1)** requirements only.

Phase 1 represents the foundational editorial engine of K2 Daily Brief.
Reader-focused refinements, automation, narrative evolution tracking, and UI simplification are explicitly excluded and reserved for later phases (see `docs/product/PRODUCT_PHASES.md`).

---

## 2. Project Overview

Purpose:
Build a locally hosted, multi-user news aggregation and AI synthesis application that generates neutral, source-cited long-form news articles from user-selected **Event Clusters**.

The system will run on the ThinkPad W550 production server and be exposed securely via Cloudflare Tunnel.

---

## 3. Scope – Version 1 (V1)

V1 delivers:

- RSS-based news ingestion
- Optional full-text fetch (see FR-009) to support higher-quality synthesis
- Automatic grouping of similar stories into **Event Clusters**
- Human-in-the-loop article selection
- AI-generated long-form news articles (target 800–1200 words; see FR-016)
- Structured 1–2 sentence summary bullets per article
- Multi-user support from day one
- Immutable generated content (articles + briefings)
- Daily Brief compilation (10–15 stories)
- Deployment on local server, accessible via Cloudflare Tunnel

---

## 4. Out of Scope (V1)

The following are explicitly excluded from V1:

- Fully automated story selection
- Automatic story updates / delta generation
- Narrative evolution tracking
- Bias scoring or political classification
- Sentiment analysis
- Real-time notifications / push alerts
- Discovering content via non-RSS crawling
- Paywall bypassing
- Auto-regeneration of previously generated articles (manual regenerate is allowed)
- Character-level source-span highlighting in generated articles (reserved for later phase)

Note: Fetching the HTML of a known article URL from an RSS item to extract readable text is **in-scope** when it does not bypass paywalls and respects normal access.

---

## 5. Functional Requirements

### 5.1 User Management

FR-001: The system shall support multiple authenticated users.  
FR-001A: The system shall provide a mechanism to create a new user account.
FR-001B: When no users exist, the system shall allow bootstrapping the first user without requiring an existing authenticated session.
FR-001C: A newly created user account may remain in a pending/cached state for up to 48 hours; if not activated within that window, it shall expire and be removed or disabled.
FR-002: Each user shall have independent topic preferences.  
FR-003: Each user shall have independent source preferences.  
FR-004: Generated articles and Daily Briefs shall be associated with a specific user.

### 5.2 RSS Ingestion

FR-005: The system shall ingest news articles via RSS feeds on a scheduled basis.  
FR-006: The system shall store all unique source URLs encountered via RSS ingestion in the database.  
FR-007: The system shall prevent duplicate storage of identical URLs.  
FR-008: Raw feed data shall never be modified after insertion.

FR-009: The system shall optionally fetch and store readable full text for RSS items (when accessible without bypassing paywalls) to improve synthesis quality.

### 5.3 Event Clustering

FR-010: The system shall group similar articles into Event Clusters using similarity logic.  
FR-011: Each Event Cluster shall represent a single real-world event.  
FR-012: Event Clusters shall be sortable by recency and number of sources.  
FR-013: Event Clusters shall be viewable for manual review.
FR-013A: Event Clusters may be formed globally, but each user’s cluster view shall be filtered by that user’s source preferences.  
FR-013B: Raw articles from user-blacklisted sources shall be hidden from that user’s cluster detail view.
FR-013C: The system shall compute and display an Event Cluster Information Gap indicator (for example: `Thin`, `Moderate`, `High Depth`) based on available source depth signals.  
FR-013D: Information Gap indicators shall be visible in cluster list/detail views to set user expectations before generation.

### 5.4 Human-in-the-Loop Article Generation

FR-014: A user shall be able to view all source articles within an Event Cluster.  
FR-015: A user shall be able to select one or more source articles.  
FR-016: The system shall generate a synthetic article using only the selected source articles.
FR-016A: Prompt policy shall prioritize factual accuracy over target length.
FR-016B: The generation service shall support a low-information mode when source depth is limited, producing a concise article instead of speculative filler.

Length rule:
- Target 800–1200 words when sufficient source text exists.
- If only RSS summaries are available, the system shall either (a) generate a shorter article or (b) clearly disclose limitations in the article preface.

### 5.5 Source-Only Enforcement (Concrete Acceptance Rule)

FR-017: Generated articles shall include a “Sources Used” section listing the URLs of the selected source articles.  
FR-018: Generated articles shall include inline citations referencing those sources (e.g., numbered [1], [2] mapped to the “Sources Used” list).  
FR-019: The system shall validate that all inline citations map to the selected sources; if validation fails, the article shall be rejected and regenerated or marked failed.

### 5.6 Article Requirements

FR-020: Articles shall maintain a neutral, fact-based tone.  
FR-021: Articles shall clearly attribute claims to sources when appropriate.  
FR-022: Finalized generated article content (headline/body/summary/sources) shall be immutable.  
FR-022A: Lifecycle status fields may transition (`queued` → `running` → `success`/`failed`) until terminal state.

### 5.7 Summary Bullets

FR-023: The system shall generate a 1–2 sentence structured summary bullet.  
FR-024: Summary bullets shall link to the full article.

### 5.8 Daily Brief Compilation

FR-025: A user shall be able to compile 10–15 generated articles into a Daily Brief.  
FR-026: Daily Briefs shall be stored as immutable snapshots.  
FR-027: Briefs shall be viewable by date and time.  
FR-028: The system shall prevent cross-user linkage (a briefing cannot include generated articles owned by another user).

### 5.9 Generation Execution and UI Behavior

FR-029: “Generate Article” shall be asynchronous in V1 (request accepted quickly; generation completes in worker/service flow).  
FR-030: Generated article lifecycle shall expose status values (`queued`, `running`, `success`, `failed`) for UI and operational visibility.  
FR-031: The UI shall show a processing state and poll for completion rather than holding a long-running HTTP request open.

### 5.10 Synthesis Audit and Transparency

FR-032: V1 shall provide a Synthesis Audit view for generated articles that maps each citation to its source article URL.  
FR-033: V1 shall store citation provenance excerpts when available and display them in the audit view as supporting evidence.  
FR-034: When excerpt provenance is unavailable, the audit view shall explicitly label the citation as source-linked without excerpt verification.

---

## 6. Non-Functional Requirements

NFR-001: The application shall run on the ThinkPad W550 production server.  
NFR-002: The application shall use MySQL 8.x only at 127.0.0.1:3306.  
NFR-003: All timestamps shall be stored in UTC.  
NFR-004: Local timezone conversion shall occur at presentation layer only.  
NFR-005: The application shall be accessible securely via Cloudflare Tunnel.  
NFR-006: All secrets shall be loaded via .env.  

NFR-007: AI prompts and responses shall be logged for traceability (including status and failure details).  
NFR-008: Background jobs shall run at-most-once per schedule slot in production.
NFR-009: Background job handlers shall be idempotent so safe replay is allowed after failures.
NFR-010: Article-generation UX shall avoid reverse-proxy timeout dependence by using asynchronous processing with status polling.

NFR-011: The web server port shall be configurable via .env.
NFR-012: Development mode shall run with Flask debug enabled.
NFR-013: The default display timezone shall be PDT when a user has not set a timezone preference.

---

## 7. Data Retention and Deletion Policy (V1)

Immutable tables (append-only; no deletes in normal operation):
- generated_articles
- generated_article_sources
- generated_article_citations
- briefings
- briefing_articles

Mutable/retention-managed tables (purge allowed by admin policy):
- raw_articles (and derived embeddings/full-text) may be purged after an admin-defined retention window only when not referenced by generated_article_sources or generated_article_citations.
- clusters/cluster_articles may be purged only if they have no generated_articles referencing them.

User lifecycle retention:
- Pending/unactivated users (created via registration but not activated) may be automatically expired after 48 hours.

Purge implementation note:
- Purge queries should use `NOT EXISTS` against both `generated_article_sources` and `generated_article_citations` to avoid deleting referenced lineage rows.

---

## 8. Success Criteria (V1)

V1 is complete when:

- Multiple users can authenticate and configure preferences.
- RSS feeds ingest successfully and Event Clusters form automatically.
- A user can generate at least 5 articles from selected Event Clusters.
- Each generated article includes structured summary bullet and a validated “Sources Used” section.
- Event Cluster views include Information Gap indicators.
- A Daily Brief of 10–15 articles can be compiled.
- Background jobs enforce at-most-once execution per schedule slot in production.
- Generation UI provides `queued/running/success/failed` visibility without long-request timeout failures.
- Generated articles expose a Synthesis Audit view with citation-to-source mapping.
- System is accessible externally via Cloudflare Tunnel.
