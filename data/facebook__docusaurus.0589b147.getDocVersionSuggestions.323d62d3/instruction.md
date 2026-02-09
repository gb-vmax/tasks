# Bug Report

### Describe the bug

I'm experiencing an issue with version suggestions in the docs plugin. When browsing documentation, the version suggestion banner is showing incorrect information - it's suggesting the current active version instead of the actual latest version of the docs.

### Reproduction

1. Set up a Docusaurus site with multiple doc versions (e.g., "1.0.0", "2.0.0", "3.0.0")
2. Navigate to an older version's documentation (e.g., version "1.0.0")
3. The version suggestion should prompt to view the latest version ("3.0.0")
4. Instead, it suggests the current version you're already viewing ("1.0.0")

This seems to be affecting the version banner functionality where users should be notified when they're viewing outdated documentation.

### Expected behavior

When viewing an older version of the documentation, the version suggestion should point to the actual latest version available, not the currently active version being viewed.

For example:
- Viewing version "1.0.0" → Should suggest "3.0.0" (latest)
- Currently it suggests "1.0.0" (current active version)

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
