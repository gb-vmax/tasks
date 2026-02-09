# Bug Report

### Describe the bug

When using `getBaseValue()` with non-object values like strings or numbers, the function is returning the wrong result. It seems like the logic for checking if a value is an object is broken - primitive values are being treated as objects when they shouldn't be.

### Reproduction

```js
import { getBaseValue } from '@mantine/core';

// This should return 'hello' but doesn't work correctly
const result1 = getBaseValue('hello');
console.log(result1); // Expected: 'hello', Actual: undefined

// This should return 42 but doesn't work correctly  
const result2 = getBaseValue(42);
console.log(result2); // Expected: 42, Actual: undefined

// Object with base property works fine
const result3 = getBaseValue({ base: 'test' });
console.log(result3); // Works as expected: 'test'
```

### Expected behavior

The function should return primitive values (strings, numbers, booleans) as-is when they're passed in. Only when an object with a `base` property is provided should it extract that property.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
