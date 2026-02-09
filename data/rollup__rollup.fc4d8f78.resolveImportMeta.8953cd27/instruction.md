# Bug Report

### Describe the bug

When using `import.meta.filename` in a config file, it returns the directory path instead of the actual file path. Similarly, `import.meta.dirname` appears to be returning incorrect values.

### Reproduction

Create a rollup config file that uses `import.meta`:

```js
// rollup.config.js
console.log('filename:', import.meta.filename);
console.log('dirname:', import.meta.dirname);

export default {
  // ... config
}
```

Expected output:
```
filename: /path/to/project/rollup.config.js
dirname: /path/to/project
```

Actual output:
```
filename: /path/to/project
dirname: /path/to/project
```

The `import.meta.filename` is returning the directory path instead of the full file path.

### Expected behavior

- `import.meta.filename` should return the full path to the current file (e.g., `/path/to/project/rollup.config.js`)
- `import.meta.dirname` should return the directory containing the file (e.g., `/path/to/project`)

Currently both seem to be returning directory paths, which breaks code that relies on getting the actual filename.

---
Repository: /testbed
