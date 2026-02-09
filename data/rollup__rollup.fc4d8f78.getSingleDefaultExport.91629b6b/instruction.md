# Bug Report

### Describe the bug

I'm experiencing an issue with default exports when there's only a single export in my bundle. The bundler seems to be skipping the first export/dependency and starting from the second one instead.

### Reproduction

```js
// module.js
export { default } from './dependency';

// dependency.js  
export default function foo() {
  return 'test';
}
```

When bundling this code, the default export is not correctly resolved. It appears to be looking at the wrong index when determining which export to use.

### Expected behavior

The bundler should correctly handle the case where there's a single default export. The first export in the list should be used, not skipped over.

### Additional context

This seems to affect scenarios where:
1. There's exactly one export in the module
2. The export is a re-export of a default from another module

The issue appears to be related to how the export block is generated - it's somehow starting iteration from the wrong position or checking the wrong condition for the exports array length.

---
Repository: /testbed
