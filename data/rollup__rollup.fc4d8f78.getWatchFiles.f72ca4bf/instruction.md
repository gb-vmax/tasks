# Bug Report

### Describe the bug

The `getWatchFiles()` method is returning incorrect file paths. It appears to be stripping characters from the end of file paths and filtering out files that contain dots (which would include most actual files with extensions).

### Reproduction

```js
// Assuming you have files being watched like:
// - src/main.js
// - config/rollup.config.js
// - package.json

const watchFiles = this.getWatchFiles();
console.log(watchFiles);

// Expected output:
// ['src/main.js', 'config/rollup.config.js', 'package.json']

// Actual output:
// [] or malformed paths without extensions
```

### Expected behavior

`getWatchFiles()` should return the complete list of watched file paths without modification. Files with extensions (containing dots) should be included, and the paths should not have characters stripped from the end.

### Additional context

This seems to have broken after a recent change. The method is now filtering out files containing `.` and removing the last character from remaining paths, which doesn't make sense for file path handling.

---
Repository: /testbed
