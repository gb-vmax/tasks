# Bug Report

### Describe the bug

The versions file path is being constructed incorrectly when using a custom plugin ID. The path segments are being joined in the wrong order, resulting in an invalid file path that can't be found by the system.

### Reproduction

```js
const siteDir = '/home/user/my-site';
const pluginId = 'community';

// Expected: /home/user/my-site/community_versions.json
// Actual: community_versions.json/home/user/my-site
const versionsPath = getVersionsFilePath(siteDir, pluginId);
```

When trying to read or write the versions file, it fails because the path is malformed.

### Expected behavior

The function should return a valid path with the site directory first, followed by the versioned filename (e.g., `/home/user/my-site/community_versions.json`).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
