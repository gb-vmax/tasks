# Bug Report

### Describe the bug

I'm experiencing an issue with form state management when clearing list state. When I try to clear the state for a list field, the behavior is incorrect - it seems like the function is returning an empty object in cases where it shouldn't, and not handling certain data types properly.

### Reproduction

```js
import { clearListState } from '@mantine/form';

// Case 1: This should preserve the state but returns empty object
const result1 = clearListState('field', 'string value');
console.log(result1); // Expected: 'string value', Got: {}

// Case 2: This should preserve the state but returns empty object  
const result2 = clearListState('field', 123);
console.log(result2); // Expected: 123, Got: {}

// Case 3: null values are not handled correctly
const result3 = clearListState('field', null);
console.log(result3); // Unexpected behavior
```

### Expected behavior

The `clearListState` function should only return an empty object when the state is actually an object that needs to be cleared. Non-object values (strings, numbers, booleans) and null should be handled correctly according to their types.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
