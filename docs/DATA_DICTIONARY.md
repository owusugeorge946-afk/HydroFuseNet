# Data Dictionary

## `dataset_summary.csv`

One-row summary of the experimental dataset and event-disjoint split.

- `benchmark`: source benchmark name.
- `target_classes`: segmentation classes.
- `total_events`: total flood events.
- `training_events`, `validation_events`, `test_events`: event counts by split.
- `source_tiles`: number of source tiles reported in the manuscript.
- `retained_patches`: total retained image patches.
- `patch_size_px`: patch dimensions.
- `stride_px`: sliding-window stride.
- `split_protocol`: splitting strategy.
- `modalities`: HydroFuseNet input streams.

## `final_test_metrics.csv`

Final selected model performance on the independent event-disjoint test set.

## `class_specific_metrics.csv`

Per-class IoU, precision, recall, and F1 for background, permanent water, and flood.

## `event_level_generalization.csv`

Performance for each independently held-out flood event.

- `event`: Copernicus EMSR activation identifier.
- `patches`: number of evaluated patches.
- `flood_fraction`: fraction of reference pixels assigned to flood.
- `accuracy`: overall event accuracy.
- `miou`: mean IoU over the three classes.
- `flood_iou`, `flood_precision`, `flood_recall`, `flood_f1`: flood-specific metrics.

## `pooled_vs_event_macro.csv`

Comparison between pixel-pooled metrics and equal-event-weighted macro metrics.

## `event_uncertainty_summary.csv`

Mean predictive uncertainty for correct and incorrect pixels by held-out event.

- `uncertainty_gap`: incorrect-pixel mean minus correct-pixel mean.

## `trained_modality_ablation.csv`

Performance of the full model and leave-one-modality-out models. Each reduced model was independently trained rather than only masked at inference.

- `configuration`: model variant.
- `removed_modality`: omitted input.
- `best_epoch`: selected checkpoint epoch for that configuration.
- `delta_flood_iou_vs_full`: Flood IoU difference relative to the full model.

## `experiment_config.json`

Machine-readable summary of the task, inputs, split, training setting, and selected checkpoint.
