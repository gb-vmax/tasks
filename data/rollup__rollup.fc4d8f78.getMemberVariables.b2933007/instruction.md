# Bug Report

### Describe the bug

I'm experiencing an issue where namespace imports are not working correctly. When importing from a module that has multiple named exports, only synthetic named exports (if any) are being included in the namespace object, while all regular named exports are missing.

### Reproduction

```js
// module.js
export const foo = 'foo';
export const bar = 'bar';
export const baz = 'baz';

// main.js
import * as myModule from './module.js';

console.log(myModule.foo); // undefined
console.log(myModule.bar); // undefined
console.log(myModule.baz); // undefined
```

Expected all three exports to be available on the namespace object, but they're all undefined. The namespace object appears to be empty or only contains synthetic exports.

### Expected behavior

All named exports from a module should be accessible when using namespace import syntax (`import * as`). The namespace object should contain all exported members.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
