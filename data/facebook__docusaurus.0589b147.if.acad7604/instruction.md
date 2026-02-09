# Bug Report

### Describe the bug

After a recent update, the tags list page is being generated even when there are no tags, which causes the build to fail. The route is created with an empty object instead of being skipped entirely.

### Reproduction

1. Create a docs version with zero tags
2. Build the site
3. The build process attempts to create a tags list route with an empty configuration object
4. This results in an error because required properties are missing from the route config

### Expected behavior

When there are no tags (or only one tag), the tags list page route should not be created at all. The function should return `null` to skip route creation, not an empty object `{}`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
