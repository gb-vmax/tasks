# Bug Report

### Describe the bug

The broken links checker is not working correctly - it seems to be ignoring all the actual routes and only keeping the 404 catch-all route. When building the site, broken links are not being detected even when they clearly exist.

### Reproduction

1. Create a Docusaurus site with multiple pages
2. Add a link to a non-existent page (e.g., `[broken link](/this-page-does-not-exist)`)
3. Run the build with broken links checking enabled
4. The build completes without reporting the broken link

### Expected behavior

The broken links checker should validate links against all actual routes in the site and report any links that point to non-existent pages. The 404 catch-all route should be filtered out during validation, not the other way around.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
