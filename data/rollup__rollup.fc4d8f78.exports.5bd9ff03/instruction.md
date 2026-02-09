# Bug Report

### Describe the bug

I'm experiencing an issue with module exports where the first export is being skipped and the wildcard re-exports (`*`) are being replaced with numeric indices instead.

When I have a module with multiple named exports, the first export in the list is not appearing in the exports array. Additionally, when using `export * from './other'`, instead of getting `'*'` in the exports list, I'm getting string numbers like `'0'`, `'1'`, etc.

### Reproduction

```js
// module.js
export const first = 1;
export const second = 2;
export const third = 3;
export * from './external';
export * from './another';

// When checking module.exports:
// Expected: ['first', 'second', 'third', '*', '*']
// Actual: ['second', 'third', '0', '1']
```

The first export (`first`) is missing from the list, and the wildcard exports are showing up as numeric strings instead of asterisks.

### Expected behavior

- All named exports should be included in the exports array
- Wildcard re-exports should appear as `'*'` in the exports list, not as numeric indices

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
