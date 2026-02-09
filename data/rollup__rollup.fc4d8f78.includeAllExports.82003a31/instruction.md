# Bug Report

### Describe the bug

When using tree-shaking with modules that have both named exports and side effects, some exports that should be included in the bundle are being incorrectly removed. This appears to affect modules where exports need to be preserved due to side effects or re-exports.

### Reproduction

```js
// module-a.js
export const foo = 'foo';
export const bar = 'bar';

// Has side effects
console.log('Module loaded');

// module-b.js
export * from './module-a.js';

// main.js
import { foo } from './module-b.js';
console.log(foo);
```

When bundling this code, the `bar` export and potentially other exports from `module-a.js` are not being included in the output, even though they should be preserved due to the module's side effects and re-export pattern.

### Expected behavior

All exports from modules with side effects should be included in the bundle when the module is imported, especially when using `export *` re-export patterns. The tree-shaking should be more conservative in these cases to avoid breaking code that relies on these exports being available.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
