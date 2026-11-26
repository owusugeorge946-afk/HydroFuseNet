# Provenance and release boundaries

## Independent matched study

The retained primary independent test includes six held-out events, 2,278 overlapping image patches, 154 source tiles and three labels (background, permanent water, flood). Treat the **event**, not the patch, as the independent unit. No original checkpoint binary or locked model forward-inference pipeline is included in this release. `data/primary_matched_event_iou.csv` and `data/primary_matched_summary.csv` summarize previously verified outputs; they are **not the predictions themselves**.

## Ancillary original experiments

The historical CSV files with original full-model performance (Flood IoU approximately 0.3448), event scores and five sensor-ablation results refer to another model checkpoint series. The original no-optical result is approximately 0.4931. These scores must not be compared as if they were paired ablations against the matched GroupNorm HydroFuseNet result (pooled IoU approximately 0.4590). Original executable exclusion-code lineage and per-run test-patch IDs are incomplete.

## Reconstructed code

The source files under `src/` are a reconstructed example and intentionally retain their historical reconstruction configurations. `src/07_ablation.py` omits enabled branches and can change the parameter structure. The archived original ablation checkpoints have matching normalized parameter key structures, so the example script must not be called the original ablation procedure.

## Reuse conditions

Data and documentation originate from a legacy deposit with a CC BY 4.0 notice, but no separate software license was assigned to the included Python source. This package does not presume that the four authors have approved a new software license. Confirm rights and licensing before public dissemination; no license to modify or redistribute the software is granted by this package alone. Third-party GEOID-Flood and satellite-data terms remain separate.
