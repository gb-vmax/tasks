# Bug Report

### Describe the bug

When using UMD format with namespaced global variables (e.g., `my.nested.module`), the generated code produces incorrect property access paths. The safe access check in the UMD wrapper is malformed, causing the module to fail to load properly in environments where the global object might not have all intermediate properties defined.

### Reproduction

Create a bundle with UMD format and specify a namespaced global variable:

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    format: 'umd',
    name: 'deeply.nested.module',
    file: 'dist/bundle.js'
  }
}
```

The generated UMD wrapper produces incorrect safe access code when checking for the existence of the global variable. Instead of properly chaining the property checks like `global && global.deeply && global.deeply.nested`, it generates a malformed path.

### Expected behavior

The UMD wrapper should generate proper safe access chains for namespaced globals, allowing the module to load correctly even when intermediate properties don't exist on the global object.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
