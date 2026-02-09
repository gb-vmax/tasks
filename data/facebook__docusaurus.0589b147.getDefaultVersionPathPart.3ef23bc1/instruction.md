# Bug Report

### Describe the bug

I'm experiencing an issue with version path generation in the docs plugin. When I have a current version configured, the path part is being set incorrectly, causing routing problems in my documentation site.

### Reproduction

Set up a docs plugin with versioning enabled:

```js
{
  versions: {
    current: {
      label: 'Next',
      // path should default to 'next' for current version
    },
    '1.0.0': {
      label: '1.0.0',
    }
  }
}
```

When navigating to the current version docs, the URL path is empty instead of `/next`. This breaks the expected routing behavior where:
- Latest stable version should have no path prefix
- Current/unreleased version should use `/next` prefix

### Expected behavior

The current version (unreleased docs) should generate a path part of `'next'` by default, not an empty string. The latest released version should have an empty path part for clean URLs.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
