# Bug Report

### Describe the bug

The versioned sidebars file path is being generated incorrectly when using a custom plugin ID. The version name and plugin ID appear to be swapped in the file path construction, causing the system to look for the wrong file.

### Reproduction

```js
// When calling getVersionSidebarsPath with:
const siteDir = '/path/to/site';
const versionName = '1.0.0';
const pluginId = 'api-docs';

// The function generates an incorrect path where the plugin ID 
// and version name are in the wrong positions
getVersionSidebarsPath(siteDir, versionName, pluginId);
```

### Expected behavior

The function should generate a path like:
```
/path/to/site/versioned_sidebars/version-1.0.0-sidebars.json
```

or with plugin ID:
```
/path/to/site/api-docs_versioned_sidebars/version-1.0.0-sidebars.json
```

Instead, it seems to be constructing the path with the version and plugin ID references mixed up, leading to files not being found during the build process.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing versioned documentation builds to fail when using multiple plugin instances with custom IDs.

---
Repository: /testbed
