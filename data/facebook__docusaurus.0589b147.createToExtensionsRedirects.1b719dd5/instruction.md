# Bug Report

### Describe the bug

The extension redirects feature is creating redirects in the wrong direction. When a URL has an extension like `.html`, the redirect is being created backwards - it's trying to redirect FROM the path without extension TO the path with extension, when it should be the other way around.

### Reproduction

```js
// Configure plugin with extension redirects
{
  fromExtensions: ['html'],
}

// For a page at /docs/intro.html
// Current behavior: Creates redirect from /docs/intro -> /docs/intro.html
// Expected behavior: Should redirect from /docs/intro.html -> /docs/intro
```

When visiting `/docs/intro.html`, instead of redirecting to the clean URL `/docs/intro`, the system tries to do the opposite redirect which doesn't make sense for the `fromExtensions` option.

### Expected behavior

When `fromExtensions` is configured with extensions like `['html']`, the plugin should:
1. Detect paths ending with those extensions
2. Create redirects FROM the extensioned path TO the clean path (without extension)

For example, `/docs/intro.html` should redirect to `/docs/intro`, not the other way around.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
