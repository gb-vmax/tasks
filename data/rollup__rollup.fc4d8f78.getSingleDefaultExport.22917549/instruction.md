# Bug Report

### Describe the bug

I'm experiencing an issue with default exports when there's exactly one named export in the module. The bundler seems to be incorrectly handling the default export in this scenario.

### Reproduction

```js
// module.js
export const foo = 'bar';
export default 'default value';
```

When bundling this module, the default export is not being handled correctly. It appears that when there's a single named export present, the logic for determining what should be used as the default export gets confused.

### Expected behavior

The default export should always be properly identified and exported, regardless of how many named exports exist in the module. A module with one named export and one default export should work the same way as a module with multiple named exports and a default export.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently, possibly after a recent update. The bundled output is missing or incorrectly referencing the default export when exactly one named export is present.

---
Repository: /testbed
