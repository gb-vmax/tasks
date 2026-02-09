# Bug Report

### Describe the bug

I'm experiencing an issue with ES module exports where namespace reexports are being incorrectly categorized. When I have a module that reexports with `export * as name from 'module'`, the bundler seems to be mishandling the export specifiers.

### Reproduction

```js
// lib.js
export const foo = 'foo';
export const bar = 'bar';

// index.js
export * as lib from './lib.js';
export { foo } from './lib.js';
```

When bundling this code, the output doesn't correctly distinguish between different types of reexports. The namespace reexport (`export * as lib`) appears to be grouped incorrectly with other export types.

### Expected behavior

The bundler should properly categorize:
- Star exports (`export * from 'module'`)
- Namespace reexports (`export * as name from 'module'`)
- Named reexports (`export { name } from 'module'`)

Each type should be handled separately and generate the correct output format.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
