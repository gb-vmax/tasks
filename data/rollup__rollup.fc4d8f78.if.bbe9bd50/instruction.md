# Bug Report

### Describe the bug

I'm encountering an issue with module exports when using dynamic imports with multiple entry points. It seems like exported variables from non-facade entry modules are not being exposed correctly in the generated bundle.

### Reproduction

```js
// entry1.js
export { foo } from './shared.js';

// entry2.js (dynamic entry)
export { bar } from './shared.js';

// shared.js
export const foo = 'foo';
export const bar = 'bar';
```

When building with multiple entries where one is dynamically imported, the exports from the dynamic entry are not accessible as expected. The facade module detection logic appears to be incorrectly determining which variables should be exposed.

### Expected behavior

All exported variables from entry modules should be properly exposed in their respective chunks, regardless of whether they are the facade module or not. Variables that are exported by non-facade entry modules should still be accessible.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
