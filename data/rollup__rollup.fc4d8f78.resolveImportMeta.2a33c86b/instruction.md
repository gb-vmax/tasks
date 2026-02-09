# Bug Report

### Describe the bug

I'm experiencing an issue where `import.meta.url` is returning the wrong value when using a config file. Instead of getting a proper file URL, it seems to be returning a directory path.

### Reproduction

Create a config file that uses `import.meta.url`:

```js
// rollup.config.js
console.log('import.meta.url:', import.meta.url);

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  }
};
```

Run rollup with this config file. The output shows an incorrect value for `import.meta.url` - it appears to be a directory path instead of the expected file URL format.

### Expected behavior

`import.meta.url` should return a proper file URL (e.g., `file:///path/to/rollup.config.js`), not a directory path. This is breaking code that relies on resolving paths relative to the config file location.

Also noticed that the object form of `import.meta` seems to have swapped values - `import.meta.url` and `import.meta.dirname` appear to have each other's values.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
