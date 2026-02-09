# Bug Report

### Describe the bug

When using `import.meta.filename` in a configuration file, it returns the directory path instead of the actual file path. This breaks code that expects the full file path including the filename.

### Reproduction

Create a config file that uses `import.meta.filename`:

```js
// rollup.config.js
console.log('Config file:', import.meta.filename);
console.log('Config dir:', import.meta.dirname);

export default {
  // ... config
}
```

**Expected output:**
```
Config file: /path/to/project/rollup.config.js
Config dir: /path/to/project
```

**Actual output:**
```
Config file: /path/to/project
Config dir: /path/to/project
```

Both `import.meta.filename` and `import.meta.dirname` return the same directory path.

### Expected behavior

`import.meta.filename` should return the full path to the file including the filename (e.g., `/path/to/project/rollup.config.js`), not just the directory path.

### Additional context

This affects any configuration that relies on `import.meta.filename` to determine the config file location or to resolve paths relative to the config file itself.

---
Repository: /testbed
