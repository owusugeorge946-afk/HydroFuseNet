# Historical results in this folder

`primary_matched_event_iou.csv` and `primary_matched_summary.csv` describe the **primary matched comparison** based on the locked six-event evaluation.

`final_test_metrics.csv`, `class_specific_metrics.csv`, `event_level_generalization.csv`, and `pooled_vs_event_macro.csv` describe the **older original-model checkpoint series** (full-model Flood IoU approximately 0.3448), not the primary GroupNorm matched-test checkpoint (pooled Flood IoU approximately 0.4590).

`trained_modality_ablation.csv` contains **ancillary separately trained screening checkpoints**. Their exact original input-exclusion logic is not authenticated by the reconstructed implementation in `src/`.

`event_uncertainty_summary.csv` belongs to an ancillary configuration; do not attribute it to the primary matched checkpoint without checkpoint-specific provenance.
