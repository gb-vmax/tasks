# Bug Report

### Describe the bug

After a recent update, the version metadata props are not being generated correctly. The `badge` property is now only included when `isLast` is true, and the `docsSidebars` prop is being generated with incomplete version information (only `versionName` instead of the full `loadedVersion` object).

### Reproduction

```js
// When creating version metadata for a non-last version
const versionMetadata = toVersionMetadataProp(pluginId, loadedVersion);

// Expected: badge property should always be present
// Actual: badge property is missing when isLast = false

// Expected: docsSidebars should receive full loadedVersion object
// Actual: docsSidebars only receives { versionName: loadedVersion.versionName }
```

### Expected behavior

1. The `badge` property should be included in version metadata regardless of whether the version is the last version or not
2. The `toSidebarsProp` function should receive the complete `loadedVersion` object, not just a partial object with only the `versionName` property

This is causing issues with version badges not displaying on older versions and sidebars potentially missing necessary context from the version data.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
