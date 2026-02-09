# Bug Report

### Describe the bug

The "Edit this page" link is pointing to the wrong URL when working with localized documentation files. When I have localized versions of my docs and set `editLocalizedFiles: true` in the plugin options, the edit link doesn't point to the localized file as expected.

### Reproduction

Setup:
1. Configure docusaurus-plugin-content-docs with `editUrl` and `editLocalizedFiles: true`
2. Create a localized version of a doc (e.g., in `i18n/fr/docusaurus-plugin-content-docs/current/`)
3. View the localized page

Expected: The "Edit this page" link should point to the localized file path
Actual: The link points to the base (non-localized) file instead

This seems to affect the logic that determines whether to use `editUrl` or `editUrlLocalized` based on the content path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
