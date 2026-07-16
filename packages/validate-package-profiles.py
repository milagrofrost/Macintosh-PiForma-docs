#!/usr/bin/env python3
"""Validate curated APT profile root files without changing package state."""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent

PROFILE_FILES = [
    "apt-system-base.txt",
    "apt-piforma-runtime.txt",
    "apt-optional-features.txt",
    "apt-development.txt",
    "apt-experiments.txt",
    "apt-compatibility.txt",
    "apt-unknown.txt",
]

FORENSIC_KERNEL_FILE = "apt-kernel-history.txt"

LOCAL_ONLY_PACKAGES = {
    "about-this-pi-forma",
    "at-ease",
    "clippy",
    "control-strip-simulator",
    "pi-forma-panel",
}

RESIDUE_PACKAGES = {"rpi-connect-lite", "tint2"}

EXACT_KERNEL_RE = re.compile(
    r"^linux-(?:base|headers|image|kbuild)-[0-9][^ ]*\+rpt(?:-|$)"
)


def read_packages(path: Path) -> list[str]:
    packages: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        packages.append(stripped)
    return packages


def apt_policy_has_repository_version(package: str) -> tuple[bool, str]:
    result = subprocess.run(
        ["apt-cache", "policy", package],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    output = result.stdout.strip()
    if result.returncode != 0:
        return False, output

    has_repo_origin = False
    for line in output.splitlines():
        stripped = line.strip()
        if re.search(r"https?://.*\bPackages\b", stripped):
            has_repo_origin = True

    candidate_none = "Candidate: (none)" in output
    return (not candidate_none and has_repo_origin), output


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    package_to_profiles: dict[str, list[str]] = defaultdict(list)

    for name in PROFILE_FILES:
        path = ROOT / name
        packages = read_packages(path)
        counts = Counter(packages)

        for package, count in sorted(counts.items()):
            if count > 1:
                errors.append(f"{name}: duplicate package {package!r}")

        for package in packages:
            package_to_profiles[package].append(name)
            if package in LOCAL_ONLY_PACKAGES:
                errors.append(f"{name}: local-only PiForma package {package!r}")
            if package in RESIDUE_PACKAGES:
                errors.append(f"{name}: dpkg residue package {package!r}")
            if EXACT_KERNEL_RE.match(package):
                errors.append(f"{name}: exact historical kernel package {package!r}")

            has_repo_version, policy = apt_policy_has_repository_version(package)
            if not has_repo_version:
                errors.append(
                    f"{name}: no configured repository version for {package!r}\\n{policy}"
                )

    kernel_path = ROOT / FORENSIC_KERNEL_FILE
    for package in read_packages(kernel_path):
        if not EXACT_KERNEL_RE.match(package):
            warnings.append(
                f"{FORENSIC_KERNEL_FILE}: non-versioned kernel entry {package!r}"
            )

    for package, profiles in sorted(package_to_profiles.items()):
        if len(profiles) > 1:
            warnings.append(
                f"cross-profile overlap: {package} appears in {', '.join(profiles)}"
            )

    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1

    print("Package profile validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
