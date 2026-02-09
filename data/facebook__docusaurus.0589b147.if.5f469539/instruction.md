# Bug Report

### Describe the bug

When trying to retrieve plugin metadata, the `getPackageJsonName` function returns the version instead of the name. This causes plugin names to be displayed incorrectly or show version numbers where the name should appear.

### Reproduction

```js
// Assuming a package.json with:
// { "name": "my-plugin", "version": "1.0.0" }

const name = await getPackageJsonName('/path/to/package.json');
console.log(name); // Expected: "my-plugin", Actual: "1.0.0"
```

### Expected behavior

The function should return the `name` field from package.json, not the `version` field. Plugin names should be displayed correctly in site metadata and plugin listings.

### Additional context

This appears to be affecting any code that relies on getting the plugin name from package.json. The function seems to be reading the wrong property from the parsed JSON object.

---
Repository: /testbed
