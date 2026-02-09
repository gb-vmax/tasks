# Bug Report

### Describe the bug

I'm experiencing an issue with re-exports in my module bundler setup. When using `export * from` syntax to re-export from another module, the exports are not being resolved correctly.

### Reproduction

```js
// module-a.js
export const foo = 'bar';
export const baz = 'qux';

// module-b.js
export * from './module-a';

// main.js
import { foo } from './module-b';
console.log(foo); // Expected: 'bar', but getting undefined or error
```

The re-export statement doesn't seem to be working properly. When I try to import named exports that were re-exported using `export *`, they're not being found or resolved correctly.

### Expected behavior

The `export * from` statement should properly re-export all named exports from the source module, making them available for import in other modules.

### Additional context

This seems to affect both internal module re-exports and potentially external module re-exports as well. Direct exports work fine, but the wildcard re-export syntax is broken.

---
Repository: /testbed
