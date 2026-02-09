# Bug Report

### Describe the bug

I'm experiencing an issue with array destructuring in export statements. When exporting variables using array patterns, some of the destructured variables are not being properly exported.

### Reproduction

```js
// test.js
export const [a, b, c, d] = [1, 2, 3, 4];
```

When trying to import these variables:
```js
import { a, b, c, d } from './test.js';
console.log(a, b, c, d);
```

Only some of the variables are available for import. It seems like not all elements in the array pattern are being recognized as exported variables.

### Expected behavior

All destructured variables in an exported array pattern should be available for import. In the example above, `a`, `b`, `c`, and `d` should all be exportable.

### Additional context

This also affects more complex patterns:
```js
export const [first, second, third] = getValues();
```

Not all of `first`, `second`, and `third` are properly exported.

---
Repository: /testbed
