# Bug Report

### Describe the bug

When trying to get site metadata, the plugin name is not being retrieved correctly. Instead of returning the package name, it appears to be returning the version field.

### Reproduction

```js
// When calling getPackageJsonName on a package.json file
const packageJsonPath = '/path/to/package.json';
const name = await getPackageJsonName(packageJsonPath);

// Expected: package name (e.g., '@docusaurus/plugin-content-docs')
// Actual: package version (e.g., '2.0.0')
```

### Expected behavior

`getPackageJsonName()` should return the `name` field from package.json, not the `version` field.

### Additional context

This seems to have broken recently - the function is returning version information when it should be returning the package name. This affects plugin metadata and potentially site configuration.

---
Repository: /testbed
