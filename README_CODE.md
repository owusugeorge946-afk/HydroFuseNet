# HydroFuseNet reconstructed reproducibility implementation

This package reconstructs the HydroFuseNet workflow from the finalized manuscript methodology and retained manuscript-ready outputs. It is **not a byte-for-byte copy of the original Google Colab notebooks**.

Verified design elements reproduced here include: five multimodal inputs (pre-event SAR, post-event SAR, SAR change, optical imagery and DEM); 256×256 patches with 128-pixel stride; event-disjoint train/validation/test evaluation; three-class segmentation; learning rate 3e-4; checkpoint selection by validation Flood IoU; uncertainty defined as `1 - max(class probability)`; and independently retrained leave-one-modality-out ablations.

## Important boundary

The exact original event identities in each split, architecture layer widths, batch size, optimizer, class-weight values, random seed and normalization constants were not recoverable. Reconstruction defaults for these items are explicitly marked in `config/experiment_config.json`. Do not describe those defaults as verified original settings.

## Prepared data layout

```text
prepared/EMSRxxx/
  pre_sar.npy
  post_sar.npy
  optical.npy
  dem.npy
  label.npy
  valid.npy   # optional
```

Run:

```bash
python src/01_preprocessing.py --input prepared --output patches
python src/02_event_disjoint_split.py --manifest patches/manifest.csv --output splits.json
python src/04_train.py --manifest patches/manifest.csv --splits splits.json --output runs/full
python src/05_evaluate.py --manifest patches/manifest.csv --splits splits.json --checkpoint runs/full/best.pt --output evaluation
python src/06_uncertainty.py --predictions evaluation/pixel_outputs.npz --output evaluation/uncertainty.csv
python src/07_ablation.py --manifest patches/manifest.csv --splits splits.json --output runs/ablations
```
