# Bug Report

### Describe the bug

The version path routing is broken after a recent change. When navigating to different documentation versions, the URL paths are being generated incorrectly. The last/latest version is now getting an empty path when it should have a version identifier, and other versions are getting swapped path values.

### Reproduction

Configuration:
```js
{
  versions: {
    'current': {},
    '2.0.0': {},
    '1.0.0': {}
  },
  lastVersionName: '2.0.0'
}
```

Expected paths:
- Version `2.0.0` (last version) → empty path ``
- Version `current` → path `next`
- Version `1.0.0` → path `1.0.0`

Actual paths:
- Version `2.0.0` (last version) → path `next` (wrong!)
- Version `current` → path `current` (wrong!)
- Version `1.0.0` → empty path (wrong!)

The logic for determining which version gets which path seems to be inverted. This affects all documentation sites using versioning and breaks existing URL structures.

### Expected behavior

The last/latest version should get an empty path (to be served at the root docs path), the current version should get the `next` path, and all other versions should use their version name as the path.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
