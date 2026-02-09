# Bug Report

### Describe the bug

I'm experiencing an issue with module exports when using dynamic imports with synthetic named exports. The facade module detection logic seems to be inverted, causing incorrect behavior when determining if a module can serve as a facade.

### Reproduction

```js
// entry1.js
export { default as foo } from './lib.js';

// entry2.js  
export * from './shared.js';

// lib.js (with synthetic named exports)
export default { bar: 'value' };

// shared.js
export const shared = 'data';
```

When bundling with multiple entry points where one uses synthetic named exports and references the same module as another entry, the facade module selection breaks down. Modules that should NOT be selected as facades are being selected, or vice versa.

### Expected behavior

The facade module should be correctly identified based on whether it exposes all necessary variables. Modules with exposed variables that don't belong to them or aren't in the export map should not qualify as facade modules.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems related to how the logic checks for exposed variables in relation to synthetic named exports and their base variables.

---
Repository: /testbed
