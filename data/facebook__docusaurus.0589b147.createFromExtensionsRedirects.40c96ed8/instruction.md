# Bug Report

### Describe the bug

I'm experiencing an issue with the client redirects plugin where extension-based redirects are being created incorrectly. The plugin seems to be generating redirects based on whether paths start with `/` instead of whether they end with `/`, which is causing unexpected redirect behavior.

### Reproduction

When configuring the plugin with extensions like `.html`:

```js
{
  fromExtensions: ['html'],
}
```

For a path like `/docs/intro`, the plugin should create a redirect from `/docs/intro.html` to `/docs/intro`.

However, the redirect generation logic appears to be checking the wrong condition - it's looking at whether the path starts with a slash rather than whether it ends with one. This means paths are being handled inconsistently.

Additionally, the check for whether a path already has an extension seems to be using `includes()` instead of `endsWith()`, which could match extensions in the middle of the path (e.g., a path containing `.html` anywhere in the string, not just at the end).

### Expected behavior

- Redirects should be created based on whether paths end with trailing slashes, not whether they start with leading slashes
- Extension checking should verify that paths END with the extension, not just contain it somewhere

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-client-redirects

---
Repository: /testbed
