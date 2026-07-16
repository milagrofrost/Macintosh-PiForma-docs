# PiForma Development Toolchains

Snapshot date: 2026-07-15 (America/New_York)

This file records non-APT development toolchain state observed during the package inventory. It is not an update instruction and no toolchains were modified.

## Rust

Rust is installed through `rustup`, not APT.

```text
Default host: aarch64-unknown-linux-gnu
rustup home: /home/frost/.rustup
installed toolchains: stable-aarch64-unknown-linux-gnu (active, default)
installed targets: aarch64-unknown-linux-gnu
rustc: 1.96.1 (31fca3adb 2026-06-26)
cargo: 1.96.1 (356927216 2026-06-26)
rustc path: /home/frost/.cargo/bin/rustc
cargo path: /home/frost/.cargo/bin/cargo
```

`cargo install --list` returned no installed Cargo commands. Project-local Rust dependencies remain part of each source checkout and are not represented as global software.

## Node And NPM

Node and npm are supplied by APT packages in the development profile. The observed versions were:

```text
node: v20.19.2
npm: 9.2.0
npm global prefix: /usr/local
npm global package set: empty
```

Project-local `node_modules` directories are not rebuild roots. They should be restored by running the appropriate project build commands after source checkouts and lockfiles are restored.
