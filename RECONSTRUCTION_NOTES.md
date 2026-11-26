# Source and model reconstruction notes

The source files in this ZIP are reconstructed code. Their optimizer, normalization, event split, architecture and ablation mechanisms must not be attributed to the original checkpoint training.

**Primary verified evaluation:** HydroFuseNet GroupNorm versus 17-channel U-Net, same six event-disjoint test events. Event-macro Flood IoU 0.357858 versus 0.309562; pooled Flood IoU 0.459021 versus 0.471923. Paired sign-flip p = 0.4375; six-event bootstrap 95% interval [-0.03078, 0.14725].

**Ancillary separate original experiments:** original full-model IoU 0.344765; `no_optical` 0.493052; other ablations documented in `data/trained_modality_ablation.csv`. Their checkpoints and selected epochs were independently audited, but the original executable modality-exclusion mechanism was not recovered.

**Reader evidence:** fixed channelwise bounds, normalization to [0,1], invalid-pixel masking, five input branches with channels [2,2,2,13,1]. Source DEM and SAR physical calibration is documented in GEOID-Flood, while unit labels are absent in locally copied raster metadata.

**Acquisition caveat:** reported optical-to-SAR intervals use source-file names; the Sentinel-2 layer can be a multi-scene per-pixel mosaic. Do not assert per-pixel acquisition gaps or causality.
