# Bug Report

### Describe the bug

When exporting multiple variable declarations in a single statement, only the second and subsequent variables are being exported. The first variable in the declaration list is not included in the module's exports.

### Reproduction

```js
// module.js
export var foo = 1, bar = 2, baz = 3;

// consumer.js
import { foo, bar, baz } from './module.js';

console.log(foo); // undefined - first variable is missing!
console.log(bar); // 2
console.log(baz); // 3
```

The same issue occurs with destructuring exports:

```js
export var { a, b } = { a: 1, b: 2 };
// 'a' is not exported, but 'b' is
```

### Expected behavior

All variables in an export declaration should be exported, including the first one. In the example above, `foo`, `bar`, and `baz` should all be available as named exports.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as it was working correctly before. Any help would be appreciated!

---
Repository: /testbed
