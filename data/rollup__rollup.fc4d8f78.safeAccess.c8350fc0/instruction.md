# Bug Report

### Describe the bug

I'm encountering an issue with UMD builds when using namespaced global variables. The generated code appears to be creating incorrect property access chains, causing the module to fail loading in certain environments.

### Reproduction

When building with UMD format and a namespaced global variable like `my.namespace.lib`, the output seems to skip the first part of the namespace chain. 

For example, with this configuration:
```js
{
  format: 'umd',
  name: 'my.namespace.lib',
  globals: {
    'external-lib': 'external.namespace.lib'
  }
}
```

The generated UMD wrapper doesn't properly check for the existence of the first namespace segment before accessing nested properties.

### Expected behavior

The UMD output should generate proper safe access checks for all segments of a namespaced global variable, ensuring that each level of the namespace exists before accessing the next level. This prevents runtime errors when the global namespace hasn't been initialized.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
