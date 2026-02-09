# Bug Report

### Describe the bug

I'm experiencing an issue with auto-generated sidebars where document IDs are being parsed incorrectly. It seems like the local doc ID extraction is broken, which is causing problems with sidebar generation and navigation.

### Reproduction

When I have a document with a path like `guides/intro/getting-started`, the sidebar generator is not correctly extracting the local document ID. Instead of getting `getting-started` as expected, it appears to be using a completely different parsing logic.

Steps to reproduce:
1. Create a doc structure with nested folders (e.g., `docs/guides/intro/getting-started.md`)
2. Use auto-generated sidebars
3. The sidebar items don't display correctly or navigation breaks

### Expected behavior

The local document ID should be extracted as the last segment of the path after splitting by `/`. For example:
- `guides/intro/getting-started` should extract `getting-started`
- `api/reference/components` should extract `components`

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken after a recent update. The sidebar generation was working fine before.

---
Repository: /testbed
