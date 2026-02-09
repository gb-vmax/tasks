# Bug Report

### Describe the bug

I'm experiencing an issue with variable exports when using destructuring or multiple variable declarations in a single export statement. It seems like only some of the exported variables are accessible, while others are either missing or pointing to the wrong values.

### Reproduction

```js
// module.js
export var { foo, bar } = { foo: 1, bar: 2 };

// or

export var first = 10, second = 20, third = 30;
```

When I try to import these variables from another module:

```js
import { foo, bar } from './module.js';
console.log(foo); // Expected: 1, but getting undefined or wrong value
console.log(bar); // Expected: 2, but getting undefined or wrong value

// or

import { first, second, third } from './module.js';
console.log(first); // Expected: 10
console.log(second); // Expected: 20, but seems to be wrong
console.log(third); // Expected: 30, but seems to be wrong
```

### Expected behavior

All variables declared in a single export statement (whether through destructuring or comma-separated declarations) should be properly exported and importable with their correct values.

### Additional context

This appears to affect export statements that declare multiple variables at once. Single variable exports seem to work fine:

```js
export var single = 5; // This works correctly
```

---
Repository: /testbed
