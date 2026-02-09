# Bug Report

### Describe the bug

When a docs version has no content path or an empty docs directory, the plugin throws an error even though it should be valid to have an empty version. This prevents the build from completing successfully.

### Reproduction

1. Create a docs version with either:
   - No `contentPath` set in the version metadata, or
   - An empty directory (no doc files)

2. Try to build the site

3. Build fails with error: `Docs version "X" has no docs! At least one doc should exist at "..."`

### Expected behavior

The plugin should handle empty doc versions gracefully instead of throwing an error. Some use cases require having version configurations without any docs initially, or having placeholder versions that will be populated later.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
