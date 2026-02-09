# Bug Report

### Describe the bug

The `getWatchFiles()` method is returning an inconsistent order of files across different calls, making it difficult to reliably track which files are being watched. The order seems to be non-deterministic and changes between invocations.

### Reproduction

```js
const plugin = {
  name: 'test-plugin',
  buildStart() {
    const watchFiles1 = this.getWatchFiles();
    const watchFiles2 = this.getWatchFiles();
    
    // These should be in the same order but they're not
    console.log(watchFiles1);
    console.log(watchFiles2);
  }
}
```

When calling `getWatchFiles()` multiple times, the returned array has files in different orders each time. This makes it hard to compare watch file lists or use them in any deterministic way.

### Expected behavior

`getWatchFiles()` should return files in a consistent, predictable order every time it's called. Ideally the array should be sorted alphabetically so the order is stable.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
