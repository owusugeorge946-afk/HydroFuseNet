# HydroFuseNet — GitHub Data Package

This repository contains the **derived tabular results and experiment metadata** associated with the HydroFuseNet manuscript:

**HydroFuseNet: Event-Generalizable Multimodal Earth Observation for Flood Segmentation and Uncertainty-Aware Mapping**

HydroFuseNet performs three-class semantic segmentation of **background**, **permanent water**, and **transient floodwater** using pre-event Sentinel-1 SAR, post-event Sentinel-1 SAR, explicit SAR change, Sentinel-2 optical imagery, and terrain elevation.

## What is included

The `data/` directory contains publication-ready CSV/JSON files for:

- dataset and event-split summary;
- final independent test metrics;
- class-specific segmentation metrics;
- held-out event generalization;
- pooled versus event-macro performance;
- event-level predictive uncertainty;
- independently trained modality ablations;
- experiment configuration metadata.

## What is not included

This package **does not redistribute the original satellite imagery, flood-reference labels, or full GEOID-Flood benchmark**. Those source data are substantially larger and may be subject to their original provider terms. Users should obtain the source benchmark and Earth-observation data from the original providers.

No raw model checkpoints are included in this package. They can be released separately if desired.

## Event-disjoint evaluation

The dataset contains 28 flood events. The final split used:

- 16 training events
- 6 validation events
- 6 independent test events

All patches from a single flood activation were assigned to only one subset, preventing event overlap between training, validation, and testing.

## Main final-model results

| Metric | Value |
|---|---:|
| Overall accuracy | 0.8946 |
| Mean IoU | 0.5988 |
| Mean F1 | 0.7244 |
| Flood IoU | 0.3448 |
| Flood precision | 0.4842 |
| Flood recall | 0.5449 |
| Flood F1 | 0.5128 |

The held-out event Flood IoU ranged from **0.7292 (EMSR314)** to **0.0118 (EMSR286)**.

## Repository structure

```text
HydroFuseNet_GitHub_Data/
├── README.md
├── CITATION.cff
├── .gitignore
├── LICENSE_NOTICE.md
├── RELEASE_CHECKLIST.md
├── data/
│   ├── dataset_summary.csv
│   ├── final_test_metrics.csv
│   ├── class_specific_metrics.csv
│   ├── event_level_generalization.csv
│   ├── pooled_vs_event_macro.csv
│   ├── event_uncertainty_summary.csv
│   ├── trained_modality_ablation.csv
│   └── experiment_config.json
└── docs/
    └── DATA_DICTIONARY.md
```

## Reproducibility note

All values in this release package are derived from the finalized manuscript-ready HydroFuseNet results. Before making the repository public, confirm that the uncertainty equation stated in the manuscript exactly matches the implementation used in the final analysis code.

## Citation

Please cite the associated manuscript. A `CITATION.cff` file is included so the repository can expose a GitHub citation panel.

## Data provenance

The manuscript uses the GEOID-Flood benchmark assembled from Copernicus Emergency Management Service flood activations, together with Sentinel-1, Sentinel-2, and terrain information. The original upstream datasets should be cited according to their source publications and provider requirements.
