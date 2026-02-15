Project: K2 Daily Brief

1. Product Philosophy
K2 Daily Brief has two conceptual layers:
	1. V1 – Newsroom Engine
	2. Final Product – Clean Daily Reader
These represent different operational modes and user experiences.
V1 is not the final user experience.

2. Phase 1 – Newsroom Engine (V1)
Purpose:
Enable controlled generation of high-quality synthetic articles using human-in-the-loop selection.
Characteristics:
	• Event Clusters visible to user
	• Manual selection of source articles
	• Explicit “Generate Article” action
	• Administrative dashboard feel
	• Structured workflow
	• Debug visibility
	• Traceability prioritized over aesthetics
V1 must include:
		• RSS ingestion
		• Event clustering
		• Manual review
		• Article generation
		• Daily Brief compilation
		• Information Gap indicator for Event Clusters (Thin/Moderate/High Depth)
		• Synthesis Audit (V1-lite: citation → source URL, with excerpt when available)
V1 must NOT include:
		• Fully automated story selection
		• Narrative evolution tracking
		• Automatic updates to events
		• Advanced bias scoring
		• UI optimized purely for passive reading
		• Exact character-level source-span highlighting in generated article text
V1 is a controlled editorial engine.

3. Phase 2 – Reader Mode (Final Product)
Purpose:
Deliver a calm, structured daily reading experience.
Characteristics:
	• Clean presentation
	• Minimal operational controls visible
	• Event Clusters abstracted away
	• Focus on reading, not managing
	• Possibly automated generation
	• Event update summaries
	• Story evolution tracking
The final product may:
		• Hide clustering mechanics
		• Auto-generate stories
		• Provide delta updates
		• Provide event evolution timelines
		• Emphasize simplicity over system transparency
		• Provide full Synthesis Audit highlighting of exact source text spans

4. Architectural Rule
All V1 development must:
	• Avoid building Phase 2 logic.
	• Avoid schema changes that assume automated generation.
	• Avoid coupling clustering to article generation.
	• Avoid introducing narrative versioning.
Phase 2 features must not exist in V1 code paths.

5. Transition Principle
The system must be architected so that:
	• Newsroom Engine logic can be retained.
	• Reader Mode can later abstract or simplify UI without schema redesign.
The final product is built on top of V1 — not alongside it.
