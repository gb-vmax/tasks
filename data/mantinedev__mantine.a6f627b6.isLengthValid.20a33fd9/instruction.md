# Bug Report

### Describe the bug

The `hasLength` validator is not working correctly. When I set an exact length requirement, it's rejecting values that match the specified length instead of accepting them. Also, the `max` option seems to be off by one - it's rejecting values that are exactly at the max length.

### Reproduction

```js
import { hasLength } from '@mantine/form';

// Case 1: Exact length validation
const validator1 = hasLength(5);
const result1 = validator1('hello'); // length is 5
// Expected: null (valid)
// Actual: error returned

// Case 2: Max length validation
const validator2 = hasLength({ max: 10 });
const result2 = validator2('exactly10!'); // length is exactly 10
// Expected: null (valid)
// Actual: error returned
```

### Expected behavior

- When using `hasLength(5)`, strings with exactly 5 characters should be considered valid
- When using `hasLength({ max: 10 })`, strings with 10 or fewer characters should be valid (a string of exactly 10 characters should pass)

### System Info

- @mantine/form version: latest
- Node version: 18.x

---
Repository: /testbed
