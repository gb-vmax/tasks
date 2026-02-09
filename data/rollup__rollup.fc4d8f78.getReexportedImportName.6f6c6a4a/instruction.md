# Bug Report

### Describe the bug

I'm experiencing an issue with re-exported modules where the generated code appears to be accessing the wrong variable names. When re-exporting default exports or namespace exports from external modules, the output seems to be swapped - it's using the namespace variable when it should use the module variable and vice versa.

### Reproduction

```js
// input.js
export { default as foo } from 'external-module';
export * as bar from 'another-module';
```

When bundling this code, the generated output uses incorrect variable references for accessing the re-exported values. The issue seems to affect both default export re-exports and namespace re-exports depending on the module format and interop settings.

### Expected behavior

The generated code should correctly reference:
- The module variable when accessing default exports in named exports mode
- The namespace variable when accessing namespace exports in the appropriate contexts

Instead, these appear to be reversed in the current output.

### System Info
- Rollup version: latest
- Module format: ESM/CJS (affects both)

---
Repository: /testbed
