# Bug Report

### Describe the bug

I'm encountering an issue where emitting files with the same name (case-insensitive) doesn't show a warning anymore. The file name conflict warning that should be logged when trying to use duplicate file names is not appearing.

### Reproduction

```js
// Emit two files with names that differ only in case
this.emitFile({
  type: 'asset',
  fileName: 'MyFile.txt',
  source: 'content1'
});

this.emitFile({
  type: 'asset', 
  fileName: 'myfile.txt',
  source: 'content2'
});
```

### Expected behavior

A warning should be logged when the second file is emitted since `MyFile.txt` and `myfile.txt` are considered the same file name on case-insensitive file systems. This warning is important to catch potential issues on Windows and macOS.

Previously this would log a file name conflict warning, but now it silently allows the duplicate without any warning.

### System Info
- Rollup version: latest
- OS: macOS

---
Repository: /testbed
