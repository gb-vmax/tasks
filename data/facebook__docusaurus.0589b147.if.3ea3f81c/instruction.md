# Bug Report

### Describe the bug

I'm experiencing an issue with extension-based redirects where paths that should be getting redirect entries are being skipped, and paths that shouldn't be getting redirects are now creating them.

### Reproduction

When configuring the client redirects plugin with extension redirects:

```js
{
  fromExtensions: ['html', 'htm'],
}
```

The following paths behave incorrectly:

1. A path like `/docs/intro` (no extension, no trailing slash) - should create redirects to `/docs/intro.html` and `/docs/intro.htm` but doesn't
2. A path like `/docs/about.md` (already has an extension) - should NOT create redirects but now does

It seems like the logic for determining when to create extension redirects is inverted or broken.

### Expected behavior

- Paths without extensions (like `/docs/intro`) should generate extension redirects
- Paths that already end with an extension (like `/docs/about.md`) should NOT generate additional extension redirects
- Empty paths and root path `/` should not generate redirects

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
