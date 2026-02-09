# Bug Report

### Describe the bug

When using the version banner/suggestion feature in docs, the suggested version link is pointing to the wrong version. Instead of suggesting the latest version when viewing an older version of the docs, it's suggesting the current version you're already viewing.

### Reproduction

Steps to reproduce:
1. Set up a Docusaurus site with multiple doc versions (e.g., `1.0.0`, `2.0.0`, `3.0.0`)
2. Navigate to an older version of a doc page (e.g., version `1.0.0`)
3. Check the version suggestion banner that appears

### Expected behavior

The version suggestion should point to the **latest version** (e.g., `3.0.0`) of the current document when viewing an older version. Instead, it's pointing back to the same version you're already viewing (e.g., `1.0.0`), which doesn't make sense as a "suggestion".

The `latestDocSuggestion` and `latestVersionSuggestion` should reference the actual latest version, not the currently active version.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
