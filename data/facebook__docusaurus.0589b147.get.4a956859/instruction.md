# Bug Report

### Describe the bug

I'm experiencing an issue with module imports where properties are not being copied correctly from the source module. When trying to access exported properties, I'm getting `undefined` values instead of the actual exported values.

### Reproduction

```js
// moduleA.js
export const foo = 'bar';
export const baz = 'qux';

// moduleB.js
import * as moduleA from './moduleA';

console.log(moduleA.foo); // Expected: 'bar', Actual: undefined
console.log(moduleA.baz); // Expected: 'qux', Actual: undefined
```

### Expected behavior

When importing all exports from a module using `import *`, all exported properties should be accessible and return their correct values. Currently, accessing these properties returns `undefined` instead of the actual exported values.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. The module structure looks correct but the property access is broken. Any help would be appreciated!

---
Repository: /testbed
