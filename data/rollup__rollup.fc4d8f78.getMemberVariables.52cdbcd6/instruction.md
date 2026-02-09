# Bug Report

### Describe the bug

I'm experiencing an issue with namespace imports where exported members are not being properly exposed. After importing a namespace, attempting to access named exports through the namespace object returns undefined, even though the exports exist in the original module.

### Reproduction

```js
// module.js
export const foo = 'test';
export const bar = 'value';

// main.js
import * as ns from './module.js';

console.log(ns.foo); // Expected: 'test', Actual: undefined
console.log(ns.bar); // Expected: 'value', Actual: undefined
```

The namespace object seems to be empty or missing the exported members. This is breaking code that relies on namespace imports to access multiple exports from a module.

### Expected behavior

Named exports should be accessible as properties on the namespace object. `ns.foo` and `ns.bar` should return the exported values.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
