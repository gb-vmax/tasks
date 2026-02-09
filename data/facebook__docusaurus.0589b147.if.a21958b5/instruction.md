# Bug Report

### Describe the bug

When using the docs plugin with a version that has no tags, the tags list route is being created incorrectly. Instead of returning `null` to skip route creation when there are no tags, an empty object `{}` is returned, which causes routing issues.

### Reproduction

1. Create a docs version with no tags defined
2. Build the site
3. The tags list route gets created even though there are no tags to display

The issue seems to be with how the plugin checks for empty tags. When `versionTags` is an empty object, the route should not be created at all, but currently an empty route config is being returned instead.

### Expected behavior

When a version has no tags (empty `versionTags` object), the `buildTagsListRoute()` function should return `null` to prevent creating a tags list route, rather than returning an empty object.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
