# Bug Report

### Describe the bug

When using `addWatchFile()` in a plugin to register files for watching, the file is only added to the watch list if it was already being watched. New files that aren't currently in the watch list are silently ignored and not tracked for changes.

### Reproduction

```js
// In a Rollup plugin
{
  name: 'my-plugin',
  buildStart() {
    // Try to watch a new file
    this.addWatchFile('./some-config.json');
  }
}
```

The file `./some-config.json` will not be watched unless it was already in the watch list. Changes to this file won't trigger a rebuild even though `addWatchFile()` was called.

### Expected behavior

Calling `addWatchFile()` should add the file to the watch list regardless of whether it was previously watched or not. The file should be tracked and changes should trigger rebuilds.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
