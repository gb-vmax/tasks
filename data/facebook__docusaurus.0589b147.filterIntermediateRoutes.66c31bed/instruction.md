# Bug Report

### Describe the bug

After a recent update, the broken links checker seems to be completely broken. It's not detecting any broken links in my documentation site, even though I know there are several invalid internal links present.

### Reproduction

1. Create a Docusaurus site with some pages
2. Add internal links that point to non-existent pages (e.g., `[broken link](/non-existent-page)`)
3. Build the site
4. Expected: broken links should be reported
5. Actual: no broken links are detected at all

It seems like the broken links detection is filtering routes incorrectly - only the 404 catch-all route is being checked instead of actual content routes.

### Expected behavior

The broken links checker should analyze all actual routes in the site and report any links pointing to non-existent pages. It should filter OUT the catch-all 404 route and check the real content routes.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
