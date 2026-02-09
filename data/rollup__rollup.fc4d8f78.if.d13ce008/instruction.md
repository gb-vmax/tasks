# Bug Report

### Describe the bug

I'm encountering an issue with plugin resolution where plugins are being skipped incorrectly. When I have multiple plugins handling module resolution, some plugins that should be running are being skipped even when they shouldn't be.

### Reproduction

```js
// Plugin configuration
const plugins = [
  pluginA(),
  pluginB(),
  pluginC()
]

// When resolving a module with skip parameter:
// source: './module.js'
// importer: '/path/to/file.js'
// skip: [{ source: './other.js', importer: '/path/to/file.js', plugin: pluginA }]

// Expected: Only pluginA should be skipped when both source AND importer match
// Actual: pluginA is being skipped even though the source is different
```

The problem occurs when using the skip mechanism in `resolveId`. If I skip a plugin for a specific source/importer combination, it seems to skip that plugin for other sources as well if just the importer matches (or vice versa).

### Expected behavior

A plugin should only be skipped when BOTH the source and importer match exactly with what was specified in the skip array. Currently it appears to skip if EITHER matches, which causes plugins to be skipped too broadly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
