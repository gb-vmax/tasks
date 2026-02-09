# Bug Report

### Describe the bug

After a recent update, the broken links checker seems to be completely broken. It's not detecting any broken links at all, even when they clearly exist in the documentation. It looks like the route filtering logic might have been affected.

### Reproduction

1. Create a Docusaurus site with some pages
2. Add links to non-existent pages (e.g., `/non-existent-page`)
3. Build the site with broken links detection enabled
4. The build succeeds without reporting any broken links

### Expected behavior

The broken links checker should detect and report links to pages that don't exist in the route configuration. Previously, this was working correctly and would fail the build when broken links were found.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
