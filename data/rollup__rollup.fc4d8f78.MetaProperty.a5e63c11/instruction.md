# Bug Report

### Describe the bug

I'm experiencing an issue with `import.meta` properties where certain meta properties are not being resolved correctly. It seems like properties with specific prefixes aren't being matched properly, causing the resolution logic to fail.

### Reproduction

```js
// In my rollup config, I'm trying to use import.meta with file references
// The following doesn't work as expected:

export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js'
  }
}

// In source file:
console.log(import.meta.ROLLUP_FILE_URL_referenceId);
```

When the code is processed, the `import.meta` property isn't being resolved to the actual file name. The meta property value just stays as-is instead of being transformed.

### Expected behavior

The `import.meta` meta properties should be correctly identified and resolved to their corresponding file names through the output plugin driver.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if this is related to any recent changes in how meta properties are handled.

---
Repository: /testbed
