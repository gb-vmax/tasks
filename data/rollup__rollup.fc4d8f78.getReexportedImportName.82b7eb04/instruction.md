# Bug Report

### Describe the bug

I'm experiencing an issue with re-exported imports when bundling modules. When re-exporting from a module that uses named exports mode, the generated code references the wrong variable, causing runtime errors.

### Reproduction

```js
// lib.js (external dependency with named exports)
export const foo = 'bar';

// index.js
export { foo } from './lib.js';
```

When bundling this with certain output formats, the generated code tries to access the default export instead of the module variable, or vice versa. This results in `undefined` values or reference errors at runtime.

### Expected behavior

Re-exported bindings should correctly reference the appropriate variable based on whether the dependency uses named exports mode or not. The generated code should work correctly regardless of the export mode of the source module.

### Additional context

This seems to affect both default exports and namespace (`*`) re-exports. The issue appears when the dependency's export mode doesn't match what the generated code expects.

---
Repository: /testbed
