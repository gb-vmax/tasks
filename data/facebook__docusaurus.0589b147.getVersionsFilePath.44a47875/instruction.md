# Bug Report

### Describe the bug

I'm encountering an issue with the versions file path generation in the docs plugin. It seems like the function that generates the path to the `versions.json` file is producing incorrect results.

### Reproduction

When using a docs plugin with a custom plugin ID, the versions file path is being generated incorrectly. For example:

```js
// With pluginId = 'community'
// Expected: [siteDir]/community_versions.json
// Actual: Something different that breaks the versioning system
```

The path generation appears to have the arguments in the wrong order, causing the plugin ID prefix to be applied incorrectly to the filename.

### Expected behavior

The function should correctly generate a path like `[siteDir]/community_versions.json` when the plugin ID is `community`. The prefix should be added to the filename, not the other way around.

### System Info

- Docusaurus version: Latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
