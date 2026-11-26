# Reconstructed code: execution scope

The scripts in `src/` are a **reference reconstruction** from earlier research materials. They are not the original HydroFuseNet GroupNorm training and no-optical training scripts.

The current implementation:
- uses `src/01_preprocessing.py` for scene-specific 2nd–98th percentile normalization; the archived matched-evaluation reader used fixed training-derived channelwise bounds;
- uses `src/02_event_disjoint_split.py` to generate a new seeded 16/6/6 event split; **this does not preserve the original event assignments**;
- creates enabled encoder branches in `src/03_hydrofusenet_model.py`; dropping a branch changes the reconstructed architecture, unlike the identical state-tensor layouts observed across archived original ablation checkpoints;
- uses a separately specified optimizer, batch size, class weights, seed and GroupNorm/BatchNorm configuration that must not be assumed to match historical training.

To inspect the entry points without running training:

```bash
python -m compileall -q src
python src/04_train.py --help
python src/07_ablation.py --help
```

Only run full training if you intend to run a **new experiment** on appropriately prepared and licensed input data. Do not attach the resulting metrics to the historical study without explicit provenance labels.

For expected prepared-data layout and example commands see `docs/DATA_DICTIONARY.md` and the sources. Training can be computationally demanding.
