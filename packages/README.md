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
- `apt-package-roles.tsv`: per-package role classification and rebuild profile.
- `apt-system-base.txt`, `apt-piforma-runtime.txt`, `apt-optional-features.txt`, `apt-development.txt`, `apt-experiments.txt`, `apt-compatibility.txt`, `apt-unknown.txt`: curated package name lists for rebuild planning.
- `local-deb-packages.tsv`: locally built Debian packages and source/deb evidence.
- `non-apt-software.tsv`: Flatpaks, AppImages, local trees/binaries, and non-APT software needed for a full rebuild story.

## Summary

Installed dpkg package rows: 2911
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

## Rebuild Profile List Counts

- system base: 92
- piforma runtime: 38
- optional: 233
- development: 600
- experiments: 71
- compatibility: 276
- unknown: 2

The machine-readable TSV and TXT files are the authoritative snapshots. Narrative documents in `docs/` explain interpretation and limitations.
