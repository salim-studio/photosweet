# Release playbook

The release playbook shared by every crafting app lives in shared-standards:
[`../shared-standards/release/playbook.md`](../../shared-standards/release/playbook.md)
(`storytold/shared-standards`, a sibling checkout; the repository is not public). It is the canonical copy; don't duplicate it here.

PhotoSweet is its reference implementation (`.github/workflows/release.yml`, `packaging/`,
`cargo xtask version`). PhotoSweet-specific details are in [releasing.md](releasing.md).
