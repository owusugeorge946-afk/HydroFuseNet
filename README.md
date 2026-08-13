# HydroFuseNet

## Event-Generalizable Multimodal Deep Learning for Flood Segmentation with Uncertainty-Aware Mapping

**Sean Field¹, Rachel Olawoyin², George Owusu Amoah²*, Francis Quayson³˒⁴**

¹ School of Computing and Department of Anthropology, University of Wyoming, USA  
² Department of Geography and Regional Planning, University of Cape Coast, Ghana  
³ Department of Land Surveying and Geospatial Science, The Hong Kong Polytechnic University, Hong Kong, China  
⁴ Research Institute for Land and Space, The Hong Kong Polytechnic University, Hong Kong, China  

*Corresponding author: George Owusu Amoah*

---

## Overview

HydroFuseNet is a multimodal deep-learning framework for event-generalizable flood segmentation from Earth-observation data. The framework integrates pre-event Sentinel-1 SAR, post-event Sentinel-1 SAR, explicit SAR change, Sentinel-2 optical imagery, and terrain elevation to distinguish three classes:

- Background
- Permanent water
- Flood

The experimental design uses an event-disjoint partitioning strategy so that flood events used for independent testing are not represented during model training or validation. This provides a stricter assessment of model transfer to previously unseen flood events.

This repository contains the derived results, experiment metadata, and supporting documentation associated with the HydroFuseNet manuscript.

## Multimodal inputs

HydroFuseNet integrates five complementary Earth-observation inputs:

| Input | Source | Information | Model role |
|---|---|---|---|
| Pre-event SAR | Sentinel-1 | VV/VH radar backscatter | Baseline surface condition |
| Post-event SAR | Sentinel-1 | VV/VH radar backscatter | Event-time surface response |
| SAR change | Derived from Sentinel-1 | Post-event versus pre-event response | Transient surface change |
| Optical imagery | Sentinel-2 | Multispectral reflectance | Surface and land-cover context |
| Elevation | DEM | Terrain elevation | Topographic context |

## Event-disjoint experimental design

The benchmark comprises **28 flood events**, partitioned into:

- **16 training events**
- **6 validation events**
- **6 independent test events**

All image patches originating from a given flood event were restricted to a single subset, preventing event overlap between training, validation, and independent testing.

Image samples were generated as **256 × 256 pixel patches** with a **128-pixel stride**.

## Final independent-test performance

| Metric | Value |
|---|---:|
| Overall accuracy | **0.8946** |
| Mean IoU | **0.5988** |
| Mean F1 | **0.7244** |
| Flood IoU | **0.3448** |
| Flood precision | **0.4842** |
| Flood recall | **0.5449** |
| Flood F1 | **0.5128** |

Performance varied substantially among unseen flood events. Event-level Flood IoU ranged from **0.7292 for EMSR314** to **0.0118 for EMSR286**, providing a direct assessment of cross-event generalization rather than performance based only on pooled pixels.

## Repository contents

The `data/` directory contains machine-readable results from the final HydroFuseNet experiments:

- dataset and event-split summary;
- final independent-test performance;
- class-specific segmentation metrics;
- held-out event generalization results;
- pooled versus event-macro evaluation;
- event-level predictive uncertainty;
- independently trained modality-ablation experiments; and
- experiment configuration metadata.

## Repository structure

```text
HydroFuseNet/
├── README.md
├── CITATION.cff
├── .gitignore
├── LICENSE_NOTICE.md
├── RELEASE_CHECKLIST.md
├── SHA256SUMS.txt
│
├── data/
│   ├── dataset_summary.csv
│   ├── final_test_metrics.csv
│   ├── class_specific_metrics.csv
│   ├── event_level_generalization.csv
│   ├── pooled_vs_event_macro.csv
│   ├── event_uncertainty_summary.csv
│   ├── trained_modality_ablation.csv
│   └── experiment_config.json
│
└── docs/
    └── DATA_DICTIONARY.md
