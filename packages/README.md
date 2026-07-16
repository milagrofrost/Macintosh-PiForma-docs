# PiForma Package Archive

Snapshot date: 2026-07-15 (America/New_York)
Host: `macintosh-piforma`
Repository: `/home/frost/Macintosh-PiForma-docs`

This directory is a non-destructive inventory of the live Raspberry Pi package state. No packages were installed, removed, purged, upgraded, marked, held, unheld, or reconfigured while generating these files.

APT marks and functional roles are separate concepts:

- Manually marked does not necessarily mean directly required.
- Automatically marked does not mean safe to remove.
- An automatic package may be essential to an active application.
- A manually installed package may represent an experiment.
- The default action for this audit is preservation and documentation.

## Files

- `apt-installed.tsv`: all installed dpkg packages with versions, architecture, APT mark, candidate, origin, and assigned category.
- `apt-manual.txt`, `apt-auto.txt`, `apt-held.txt`: exact sorted APT mark snapshots.
- `apt-sources.txt`: sanitized APT source, architecture, policy, and no-candidate summary.
- `apt-package-roles.tsv`: forensic per-package role classification and rebuild-profile interpretation for every dpkg status row.
- `apt-kernel-history.txt`: forensic record of exact versioned kernel packages present in dpkg status; not a normal install root list.
- `dpkg-residue.txt`: dpkg config/status residue rows that are not install recommendations.
- `local-deb-packages.tsv`: locally built Debian packages and source/deb evidence with current checkout commits kept separate from verified build provenance.
- `non-apt-software.tsv`: Flatpaks, AppImages, local trees/binaries, Rust/toolchain notes, and non-APT software needed for a full rebuild story.
- `python-environments.tsv`: Python distribution ownership inventory. This is not a pip restore manifest.
- `development-toolchains.md`: Rust, Cargo, Node, and npm development toolchain evidence.
- `apt-system-base.txt`, `apt-piforma-runtime.txt`, `apt-optional-features.txt`, `apt-development.txt`, `apt-experiments.txt`, `apt-compatibility.txt`: curated top-level APT installation roots. These intentionally omit dependency closure, local `.deb` packages, residue rows, and historical kernel versions.
- `validate-package-profiles.py`: read-only validator for curated profile files.

## Summary

dpkg status rows: 2911
Installed/held-installed package rows: 2909 (`ii`: 2908, `hi`: 1)
Config/status residue rows: 2 (`rc`: 2)
Manual marks: 401
Automatic marks: 2508
Held packages: libsdl2-dev

## Classification Totals

- `base-os`: 41
- `compatibility`: 14
- `dependency`: 1593
- `development-toolchain`: 600
- `experiment`: 71
- `feature-runtime`: 16
- `foreign-architecture`: 262
- `kernel-history`: 20
- `local-deb`: 5
- `optional-utility`: 227
- `piforma-core-runtime`: 29
- `raspberry-pi-hardware`: 31
- `unknown`: 2

## Curated Installation Root Counts

Counts below ignore comments and blank lines. They are top-level packages to request from APT, not dependency closures.

- system base roots: 36
- piforma runtime roots: 18
- optional feature roots: 31
- development roots: 78
- experiment roots: 25
- compatibility roots: 9
- unknown roots: 0
- historical kernel status entries: 20

Run `python3 packages/validate-package-profiles.py` after editing curated profile files. The validator is read-only and rejects local-only PiForma packages, residue rows, missing repository candidates, and exact historical kernels in normal profiles.

The machine-readable TSV and TXT files are the authoritative snapshots. Narrative documents in `docs/` explain interpretation and limitations.
