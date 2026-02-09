# Bug Report

### Describe the bug

After a recent update, plugin file paths are not being resolved correctly during the translation extraction process. When a plugin provides multiple paths through `getPathsToWatch()`, only the first path gets resolved relative to the plugin directory, while subsequent paths are left as-is. This causes the translation extractor to look for files in incorrect locations.

### Reproduction

1. Create a plugin that returns multiple paths from `getPathsToWatch()`:
```js
getPathsToWatch() {
  return [
    'src/components',
    'src/theme',
    'lib/utils'
  ];
}
```

2. Run translation extraction
3. Only files from the first path (`src/components`) are found correctly
4. Files from other paths fail to be located because they're not resolved relative to the plugin path

### Expected behavior

All paths returned by `getPathsToWatch()` should be resolved relative to the plugin's base path, not just the first one. The translation extractor should be able to find source files in all specified directories.

Additionally, there seems to be an issue with the theme path logic - it's only being added when `codePaths` is empty, which doesn't make sense if a plugin already has paths to watch.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
