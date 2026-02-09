# Bug Report

### Describe the bug

I'm experiencing an issue with version banners in the docs plugin. When viewing the current/latest version of documentation, an empty string banner is being displayed instead of no banner at all. This creates unwanted whitespace or rendering artifacts in the UI.

### Reproduction

```js
// Setup docs with versioning enabled
const versionContext = {
  versionName: '2.0.0',
  lastVersionName: '2.0.0',
  versionNames: ['2.0.0', '1.0.0']
}

// When checking the default version banner
const banner = getDefaultVersionBanner(versionContext)

// Expected: null (no banner)
// Actual: '' (empty string, causing rendering issues)
```

### Expected behavior

When viewing the current/latest version of documentation, no banner should be displayed at all. The function should return `null` to indicate no banner is needed, not an empty string.

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

This seems to have started recently and is affecting the visual appearance of our documentation site. The empty string is being treated as a valid banner value rather than "no banner needed".

---
Repository: /testbed
