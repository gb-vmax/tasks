# Bug Report

### Describe the bug

When emitting files with the same name (case-insensitive), the second file overwrites the first one instead of logging a warning. The file name conflict detection seems to be inverted - warnings are shown when there's no conflict, and files are silently overwritten when there should be a conflict.

### Reproduction

```js
this.emitFile({
  type: 'asset',
  fileName: 'myfile.txt',
  source: 'content 1'
});

this.emitFile({
  type: 'asset',
  fileName: 'MyFile.txt', // Different case
  source: 'content 2'
});
```

### Expected behavior

- A warning should be logged when trying to emit a file with a name that conflicts (case-insensitive) with an existing file
- The second file should not overwrite the first one

### Actual behavior

- No warning is logged for the actual conflict
- The second file overwrites the first one
- Warnings appear to be logged when there's no conflict (incorrect behavior)

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
