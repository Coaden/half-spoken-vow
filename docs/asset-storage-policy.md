# Asset Storage Policy

## Purpose

Preserve costly or irreplaceable creative assets without allowing ordinary Git history to become an audio/video archive.

## Storage classes

### Normal Git

Commit:

- manuscripts, WorldState files, project skills, scripts, prompts, and production documentation;
- small working images and approved covers;
- asset manifests, checksums, licenses, and generation metadata;
- historical text snapshots that materially document the manuscript's development.

The current cover and banner collection is small enough for normal Git. Do not migrate these files merely to make the first repository more complicated.

### Git Large File Storage

Use Git LFS for irreplaceable binary masters that must remain directly associated with a source commit, including:

- WAV, MP3, M4A, and M4B narration masters;
- MP4 and MOV masters that remain part of active production;
- PSD, TIFF, or unusually large source-image files;
- other non-rebuildable binary files whose revision history matters.

Git LFS must be installed and its tracking rules committed before the first applicable master is added. Do not commit such a file to ordinary Git and plan to migrate it later; removing it from the visible tree does not remove it from Git history.

### External archive or object storage

Use external archival storage for:

- large collections of completed audio and video masters;
- raw generation batches and rejected-but-worth-preserving source material;
- delivery packages that do not need to be retrieved with every repository clone;
- redundant disaster-recovery copies of irreplaceable assets.

For every externally stored canonical asset, commit a manifest entry containing its stable path or object identifier, SHA-256 checksum, byte size, media type, origin or generation method, rights information when applicable, and relationship to the relevant book or episode.

### GitHub Releases

Attach completed distribution artifacts such as EPUB files to a tagged GitHub Release. These packages are outputs of a specific manuscript version and should not inflate ordinary Git history.

### Ignored production output

Do not commit caches, temporary renders, intermediate exports, generated build HTML, Python bytecode, or rebuildable local EPUB files. The repository's `.gitignore` enforces the current exclusions.

## Backup rule

Git history is version control, not the sole backup. Keep at least one independent backup of the repository and all externally stored irreplaceable masters.

## Current transition

The pre-continuity-audit episode snapshot is included in the initial commit as a one-time historical baseline. After repository creation, use commits, tags, or explicit archival branches instead of creating further full-manuscript backup directories.

