# Bug Report

### Describe the bug

When exporting multiple variable declarations in a single statement, only the second and subsequent variables are being exported, while the first variable in the declaration list is being skipped.

### Reproduction

```js
// module.js
export var foo = 1, bar = 2, baz = 3;
```

When trying to import from this module:
```js
import { foo, bar, baz } from './module.js';

console.log(foo); // undefined or not exported
console.log(bar); // 2
console.log(baz); // 3
```

The first variable `foo` is not properly exported, but `bar` and `baz` work as expected.

### Expected behavior

All variables in the export declaration should be exported and accessible:
```js
import { foo, bar, baz } from './module.js';

console.log(foo); // 1
console.log(bar); // 2
console.log(baz); // 3
```

This also affects destructuring exports:
```js
export var { a, b } = obj;
// Only 'b' is exported, 'a' is missing
```

### Additional context

This seems to be a regression as it was working correctly before. Single variable exports still work fine:
```js
export var foo = 1; // This works
```

---
Repository: /testbed
