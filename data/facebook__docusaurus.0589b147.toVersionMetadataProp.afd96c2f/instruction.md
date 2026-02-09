# Bug Report

### Describe the bug

The `isLast` property in version metadata appears to have inverted logic - it returns `true` when a version is NOT the last version, and `false` when it IS the last version. This is causing issues when trying to conditionally render components or apply styles based on whether a documentation version is the latest one.

### Reproduction

```js
// When checking if a version is the last/latest version
const versionMeta = toVersionMetadataProp(pluginContext, loadedVersion);

// Expected: isLast should be true for the latest version
// Actual: isLast is false for the latest version
console.log(versionMeta.isLast); // Returns opposite of expected value
```

### Expected behavior

The `isLast` property should return `true` when the version is the last/latest version in the documentation, and `false` otherwise. This would allow proper conditional rendering like:

```js
{versionMeta.isLast && <LatestVersionBadge />}
```

### Additional context

This seems to affect any logic that depends on identifying the latest documentation version, potentially causing UI elements meant for the latest version to appear on older versions instead, or vice versa.

---
Repository: /testbed
