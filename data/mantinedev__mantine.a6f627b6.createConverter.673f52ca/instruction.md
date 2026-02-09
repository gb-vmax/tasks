# Bug Report

### Describe the bug

I'm experiencing an issue with the unit converter utility where string values like `'0'` are not being handled correctly. When I pass the string `'0'` to functions that use the converter (like `rem()` or `em()`), it's not returning the expected `'0rem'` or `'0em'` output anymore.

### Reproduction

```js
import { rem } from '@mantine/core';

// This doesn't work as expected
const result = rem('0');
console.log(result); // Expected: '0rem', but getting something else

// Numeric 0 still works fine
const result2 = rem(0);
console.log(result2); // Works: '0rem'
```

### Expected behavior

Both `rem(0)` and `rem('0')` should return `'0rem'`. The string version of zero should be treated the same as the numeric version since they represent the same value.

### Additional context

This seems to have broken recently. I use string values from CSS-in-JS libraries that sometimes pass dimensions as strings, and the string `'0'` is a common case that should be handled properly.

---
Repository: /testbed
