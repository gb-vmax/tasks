# Bug Report

### Describe the bug

When viewing the current/latest version of documentation, a version banner is unexpectedly appearing. The banner should not be displayed for the current version, but it's showing up anyway.

### Reproduction

```js
const versionContext = {
  versionName: 'current',
  lastVersionName: 'current',
  versionNames: ['1.0', '2.0', 'current']
}

// Expected: no banner for current version
// Actual: banner is displayed
const banner = getDefaultVersionBanner(versionContext)
```

### Expected behavior

When `versionName` matches `lastVersionName` (i.e., viewing the current/latest version), no version banner should be displayed. The function should return `null` to indicate no banner is needed.

### System Info

- Docusaurus plugin: docusaurus-plugin-content-docs
- This affects version banner display logic

---
Repository: /testbed
