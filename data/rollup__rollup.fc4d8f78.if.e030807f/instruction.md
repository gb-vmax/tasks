# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports in ES modules where the generated export statements are completely wrong. It seems like the logic for determining which type of re-export to use has been inverted.

### Reproduction

When bundling a module that re-exports from another module, the output is incorrect:

```js
// input module
export * from './other-module';
export { foo } from './another-module';
export { default as bar } from './third-module';
```

After bundling, the re-exports are being categorized incorrectly. Specifically:
- Star exports (`export * from`) are not being recognized properly
- Namespace re-exports are being confused with regular named re-exports
- The conditions for identifying different re-export types appear to be inverted

This results in malformed output that doesn't match the expected ES module syntax.

### Expected behavior

The bundler should correctly identify and handle:
1. Star exports (`export * from 'module'`) - when `reexported === '*'`
2. Namespace re-exports (`export * as name from 'module'`) - when `imported === '*'`
3. Named re-exports (`export { name } from 'module'`) - all other cases

Each type should be processed and output according to its correct category.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
