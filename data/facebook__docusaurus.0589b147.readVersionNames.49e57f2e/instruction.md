# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin versioning behavior. When I have `disableVersioning: true` in my plugin options on a versioned site (with a `versions.json` file), the plugin doesn't throw an error as expected. It seems like the validation is backwards.

Additionally, when `includeCurrentVersion` is set to `true` and the current version is already listed in `versions.json`, it still gets added again to the beginning of the versions array, resulting in duplicate entries.

### Reproduction

**Scenario 1:**
1. Create a versioned docs site with a `versions.json` file
2. Set `disableVersioning: true` in the docs plugin options
3. Build the site

Expected: Should throw an error about using `disableVersioning: true` on a versioned site
Actual: No error is thrown, plugin proceeds normally

**Scenario 2:**
1. Have a `versions.json` file that includes `"current"` in the versions array
2. Set `includeCurrentVersion: true` in plugin options
3. Build the site

Expected: The current version should only appear once in the final versions list
Actual: The current version appears twice (duplicated at the beginning)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
