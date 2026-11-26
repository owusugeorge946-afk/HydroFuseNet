# HydroFuseNet: Source code and research results

**Associated research article:** HydroFuseNet: Cross-Event Transferability, Multimodal Segmentation, and Comparative Reliability Across Unseen Flood Events

**Authors:** George Owusu Amoah (corresponding author), Rubayet Bin Mostafiz, Rachel Olawoyin, Francis Quayson.

**Correspondence:** george.amoah003@stu.ucc.edu.gh

## Release scope

This repository provides a **reconstructed reference implementation** of a multimodal flood-segmentation workflow, preserved ancillary experiment summaries, and machine-readable summary results from the matched independent-test comparison. The source files in `src/` **were not authenticated as the original code used to train the archived HydroFuseNet or modality-ablation checkpoints**. Running these scripts with their current defaults must not be expected to regenerate the reported manuscript results.

The archived results fall into two distinct groups:

1. **Primary matched evaluation**: the separately trained GroupNorm HydroFuseNet and 17-channel U-Net, evaluated on six unseen events with matched reference labels. Equal-event Flood IoU: 0.3579 and 0.3096; pooled Flood IoU: 0.4590 and 0.4719, respectively. Paired sign-flip p = 0.4375, with 95% paired-event bootstrap interval [-0.0308, 0.1473].
2. **Ancillary original-model and modality-screening records**: original full model pooled Flood IoU 0.3448 and no-optical configuration 0.4931. These are different checkpoints from the primary matched experiment. The precise modality-exclusion source implementation and per-run test-patch identity have not been fully reconstructed.

The test subset includes 2,278 overlapping patches from six independent flood events and 154 distinct source tiles; all retained data include 26,111 patches from 28 events. No additional independent events are introduced in this package.

## Data files

- `data/primary_matched_event_iou.csv` — six-event, two-model IoU comparisons from the locked evaluation.
- `data/primary_matched_summary.csv` — matched model aggregates and significance analysis.
- `data/ancillary_record_guide.md` — clarifies the provenance of historical CSV tables, including `final_test_metrics.csv` and `trained_modality_ablation.csv`.
- Existing CSVs in `data/` — ancillary original-model optimization, segmentation and modality-screening results as documented.

## Reference implementation

The `src/` folder contains a **reconstruction**, not an original training snapshot. It uses a scene-level percentile preprocessing approach, a configurable branch-removal architecture and a seeded event split; these choices are not necessarily the same as the archived experiments. Its command-line entry points are documented in `README_CODE.md`. The runnable reference code is provided to inspect one possible modeling workflow, **not as an exact reproduction claim**.

Original reader evidence instead supports 17 stored channels and five derived branches: pre-SAR 2, post-SAR 2, normalized SAR change 2, optical 12 plus a derived valid-band mean 1, and DEM 1. The matched evaluation used fixed channelwise normalization bounds.

For full reproduction of manuscript figures and metrics, the specific archived checkpoints, manifests, preprocessing bounds and evaluation code would need to be deposited together. These are not present in this lightweight package.

## External inputs

The source GEOID-Flood benchmark, optical/radar satellite imagery and third-party elevation products are **not included**. Obtain the dataset from its originating providers and comply with all applicable terms. The model checkpoint files are not included. No credentials or account tokens are included.

## Citation and deposit

`CITATION.cff` contains the four-author software citation metadata. See `ZENODO_DEPOSIT_INSTRUCTIONS.md` for the workflow and `PROVENANCE_AND_SCOPE.md` for source-to-result boundaries. A DOI is **not supplied before Zenodo actually assigns one**.

## Release version

Reconstructed reference implementation and evidence summary, version **1.1.0**, 2026.
