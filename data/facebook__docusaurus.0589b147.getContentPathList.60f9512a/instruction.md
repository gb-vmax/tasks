# Bug Report

### Describe the bug

After a recent update, pages from the default content path are no longer being loaded. Only localized pages are being detected and rendered. This means that if I have pages in my main pages directory but no localized versions, they simply don't show up on the site.

### Reproduction

1. Create a page in the default pages directory (e.g., `src/pages/my-page.md`)
2. Don't create a localized version of this page
3. Build or run the site
4. The page is not accessible and doesn't appear in the generated site

### Expected behavior

Both the default content path and localized content path should be scanned for pages. Pages in the default directory should be loaded even when there's no localized version available.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-pages
- Node version: 18.x

---
Repository: /testbed
