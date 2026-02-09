# Bug Report

### Describe the bug

I'm experiencing incorrect behavior with re-exported imports when using different module formats. The generated code seems to be accessing the wrong variable names for default exports and namespace imports, causing runtime errors.

### Reproduction

When bundling modules with re-exports, the output uses incorrect variable references depending on the export mode:

```js
// input module
export { default as foo } from './external';
export * as bar from './another-external';
```

After bundling, the generated code references the wrong variables - it uses the namespace variable when it should use the module variable and vice versa. This causes the exports to be undefined or point to the wrong objects at runtime.

### Expected behavior

Re-exported default exports and namespace imports should correctly reference their corresponding variables in the generated bundle. The code should work correctly regardless of whether the dependency uses named exports mode or not.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundle builds successfully but the exports are broken at runtime.

---
Repository: /testbed
