# Bug Report

### Describe the bug

I'm experiencing an issue with broken link detection where valid pathnames are being incorrectly cached. When checking if a pathname matches any route, the system is adding pathnames to the `validPathnames` cache even when they don't actually match any route.

### Reproduction

1. Set up a Docusaurus site with broken link detection enabled
2. Create a link to a non-existent route (e.g., `/some/invalid/path`)
3. The broken link checker doesn't properly detect this as broken because the pathname gets added to `validPathnames` cache regardless of whether it matched a route

### Expected behavior

Only pathnames that actually match existing routes should be added to the `validPathnames` cache. Non-matching pathnames should not be cached as valid, and the function should return `false` when a pathname doesn't match any route.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like it could lead to false negatives in broken link detection, where invalid links are not being reported as broken.

---
Repository: /testbed
