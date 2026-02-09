# Bug Report

### Describe the bug

When a docs version has no documents, the error message shows an incorrect path. The error message references `contentPath` but should be showing `contentPathLocalized` instead, which leads to confusion when trying to locate where docs should be placed, especially in multi-language setups.

### Reproduction

1. Set up a Docusaurus site with versioned docs and i18n enabled
2. Create a version that has no docs in a localized folder
3. Build the site
4. The error message will point to the wrong directory path

### Expected behavior

The error message should display the correct localized content path (`contentPathLocalized`) so users know exactly where to add their documentation files. This is particularly important for internationalized sites where the actual content path differs from the base content path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
