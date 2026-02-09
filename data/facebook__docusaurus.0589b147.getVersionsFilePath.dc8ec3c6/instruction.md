# Bug Report

### Describe the bug

The `versions.json` file is being looked up in the wrong directory. Instead of being placed in the site directory (e.g., `[siteDir]/versions.json` or `[siteDir]/community_versions.json`), it's now being placed in the parent directory of the site directory.

### Reproduction

```js
// Given a site directory: /path/to/my-website
// Plugin ID: 'community'

// Expected file path: /path/to/my-website/community_versions.json
// Actual file path: /path/to/community_versions.json
```

This breaks version management for docs plugins, as the versions file cannot be found in the expected location.

### Expected behavior

The `versions.json` file (or `[pluginId]_versions.json` for non-default plugins) should be created/looked up directly in the site directory, not in its parent directory.

For example:
- Default plugin: `[siteDir]/versions.json`
- Custom plugin with ID `community`: `[siteDir]/community_versions.json`

### System Info

This appears to affect all configurations using versioned docs.

---
Repository: /testbed
