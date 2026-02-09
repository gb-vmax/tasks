# Bug Report

### Describe the bug

The versioned docs directory path is being constructed incorrectly. When trying to access versioned documentation, the path structure seems to be wrong - the site directory and version folder name are in the wrong order, and the "version-" prefix is missing from the version folder name.

### Reproduction

```js
const pluginId = 'default';
const siteDir = '/my-site';
const versionName = '1.0.0';

const docsPath = getVersionDocsDirPath(siteDir, pluginId, versionName);
// Returns an incorrect path structure
```

### Expected behavior

The function should return a path like `/my-site/versioned_docs/version-1.0.0` but it's generating something different. The versioned docs directory should be located under the site directory with the proper "version-" prefix.

### System Info
- Docusaurus plugin: docusaurus-plugin-content-docs
- Node version: 18.x

---
Repository: /testbed
