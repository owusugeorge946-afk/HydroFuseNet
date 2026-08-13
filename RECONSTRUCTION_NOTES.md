# Reconstruction notes

Verified from retained HydroFuseNet manuscript materials:
- 28 events; 16 train, 6 validation, 6 held-out test.
- 26,111 retained patches from 771 source tiles.
- 256×256 patches; stride 128.
- Pre-SAR, post-SAR, SAR-change, optical and DEM inputs.
- Background, permanent-water and flood classes.
- Python/PyTorch; NVIDIA A100.
- Learning rate 3e-4; maximum 10 epochs.
- Best finite validation Flood IoU checkpoint; final epoch 6 with validation Flood IoU 0.5842.
- Class weighting.
- Predictive uncertainty = 1 - maximum predicted class probability.
- Five independently retrained leave-one-modality-out configurations.

Not exactly recovered: event identities for each split, exact network layer widths, batch size, optimizer, weight decay, class-weight values, random seed and normalization constants. These are reconstruction defaults and must not be represented as verified original settings.
