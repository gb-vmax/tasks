# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where versioned docs files are being placed in the wrong directory structure. It looks like the plugin ID prefix logic got inverted somehow.

### Reproduction

When using a non-default plugin instance (e.g., `pluginId: 'community'`), the versioned docs and sidebars are now being written to paths without the plugin ID prefix, which causes conflicts with the default plugin instance.

Expected behavior:
- Default plugin (no pluginId): Files should be in `versioned_docs/`, `versioned_sidebars/`
- Named plugin (e.g., `community`): Files should be in `community_versioned_docs/`, `community_versioned_sidebars/`

Actual behavior:
- Default plugin: Files are being prefixed with `default/` (e.g., `default/versioned_docs/`)
- Named plugin: Files have no prefix and go directly to `versioned_docs/`

This is causing the plugin instances to write to each other's directories.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
