# Bug Report

### Describe the bug

When using watch mode with a config file, rapid successive changes to the config file can cause the wrong configuration to be loaded. The config file data and revision counter get out of sync, leading to unexpected behavior where an older config is used instead of the latest one.

### Reproduction

1. Start rollup in watch mode with a config file
2. Make a change to the config file
3. Quickly make another change to the config file before the first reload completes
4. The second change might be ignored or the wrong config version gets applied

Example scenario:
```js
// Initial config
export default { ... }

// Change 1: update output format
// Change 2: update plugins (done quickly after change 1)
// Result: config reload uses data from change 1 instead of change 2
```

### Expected behavior

The watcher should always reload with the most recent config file data, even when multiple changes happen in quick succession. The revision tracking should ensure that only the latest config is applied.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
