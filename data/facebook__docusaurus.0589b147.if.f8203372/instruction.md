# Bug Report

### Describe the bug

The site metadata extraction is not working correctly after a recent update. When trying to read package information, the version and name fields are returning `undefined` even though the package.json file exists and contains valid data.

### Reproduction

```js
// Given a valid package.json file with:
{
  "name": "my-docusaurus-plugin",
  "version": "1.0.0"
}

// The getPluginVersion function returns undefined
// The getPackageJsonName function also returns undefined
```

### Expected behavior

When a package.json file exists with a standard `version` field (as a string) and `name` field, these values should be correctly extracted and returned by the metadata functions. The version should be read directly as a string property, not as a nested object.

### Additional context

This seems to have broken the ability to properly detect plugin versions and names in the site metadata. The functions appear to be looking for the wrong structure in the package.json file.

---
Repository: /testbed
