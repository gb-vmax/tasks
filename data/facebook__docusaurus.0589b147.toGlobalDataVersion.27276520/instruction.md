# Bug Report

### Describe the bug

I'm experiencing an issue with the docs global data structure where some documents are not appearing in the version's `docs` array as expected. It seems like documents are being filtered out incorrectly, causing certain docs to be missing from the global data.

### Reproduction

1. Set up a Docusaurus site with multiple versions
2. Create several documentation pages with valid IDs
3. Build the site and inspect the global data
4. Notice that some legitimate docs are missing from the `docs` array in the version data

The issue appears to be related to how docs are being combined with category generated indices. Regular documentation pages that should be included are being filtered out.

### Expected behavior

All documentation pages should be present in the version's `docs` array in the global data, along with any category generated indices. The filtering logic should only remove items that genuinely shouldn't be included, not valid documentation pages with proper IDs.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like it might be a regression from a recent change. Any help would be appreciated!

---
Repository: /testbed
