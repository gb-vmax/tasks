# Bug Report

### Describe the bug

I'm experiencing an issue with `import.meta` file references where certain file metadata properties are not being resolved correctly. Specifically, when using `import.meta` with properties that start with a file prefix, some of them don't get the expected reference ID assigned.

### Reproduction

```js
// In a module file
const fileUrl = import.meta.ROLLUP_FILE_URL_somefile;
console.log(fileUrl); // Should resolve to the file reference, but doesn't work
```

It seems like properties with certain prefixes work fine, but others that should also be supported are being ignored. The property gets accessed but the internal reference tracking doesn't happen as expected.

### Expected behavior

All `import.meta` file-related properties with the appropriate prefixes should be properly tracked and assigned reference IDs, regardless of which specific prefix they use.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
