# Zenodo deposit workflow

1. Confirm the four authors, affiliations, source-code rights and release licensing. The source scripts have **no verified software license** in the supplied archive.
2. If depositing this ZIP directly, in Zenodo select **New upload**, Resource type **Software**, provide the four authors in the order in `CITATION.cff`, the version **1.1.0**, and the exact software title from `CITATION.cff`. Copy the source/provenance limitation into the description. Do not claim the package fully regenerates the paper.
3. If using GitHub integration instead, first update the connected GitHub repository with the same files, then archive a tagged release. Zenodo can use `CITATION.cff`; if a `.zenodo.json` is also present it overrides `CITATION.cff`. This release includes **no** `.zenodo.json` to avoid duplicate metadata.
4. Upload the versioned ZIP; verify its checksum, copyright/licensing selection, and all author records. Review before publishing because DOI creation and public visibility occur on publication.
5. Once Zenodo assigns a DOI, add it to the manuscript's code-availability statement and update `CITATION.cff` / the release record as appropriate; do not type a placeholder DOI into publication-ready bibliographic citations.

**Scope:** This deposit preserves a reconstructed reference implementation with summarized archived results. It does **not** include original checkpoint binaries, exact original ablation training code, or full satellite data.
