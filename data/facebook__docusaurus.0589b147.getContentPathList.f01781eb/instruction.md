# Bug Report

### Describe the bug

When using localized content paths in the pages plugin, the `getContentPathList` function returns an incorrect array. If `contentPathLocalized` is defined, it only returns `contentPath` instead of including both paths. This causes the localized content to be ignored and only the base content path to be processed.

### Reproduction

```js
const contentPaths = {
  contentPath: '/path/to/pages',
  contentPathLocalized: '/path/to/pages/en'
}

const result = getContentPathList(contentPaths)
// Returns: ['/path/to/pages']
// Expected: ['/path/to/pages/en', '/path/to/pages']
```

### Expected behavior

When `contentPathLocalized` is defined, the function should return both the localized path and the base content path in the correct order. The localized path should come first so it takes precedence, followed by the base path as a fallback.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking i18n functionality since localized pages are not being loaded when they exist.

---
Repository: /testbed
