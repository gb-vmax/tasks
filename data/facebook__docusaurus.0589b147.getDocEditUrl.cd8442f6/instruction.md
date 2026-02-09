# Bug Report

### Describe the bug

When using the `editUrl` option as a string in the docs plugin configuration, the edit URL generation doesn't work correctly for localized content. The edit URLs are being generated incorrectly based on the localization status of the document.

### Reproduction

Set up a Docusaurus site with:
1. Multiple locales configured
2. `editLocalizedFiles: true` in the docs plugin options
3. A string value for `editUrl` (e.g., 'https://github.com/user/repo/edit/main/')

When viewing a non-localized document, the edit URL is incorrectly pointing to the localized version path instead of the base version path.

Expected: Non-localized docs should use `versionMetadata.editUrl`
Actual: Non-localized docs are using `versionMetadata.editUrlLocalized`

### Expected behavior

The edit URL should correctly reflect whether the document is localized or not:
- For localized documents with `editLocalizedFiles: true`, use the localized edit URL
- For non-localized documents, use the base edit URL

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
