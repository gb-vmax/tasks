# Bug Report

### Describe the bug

The `hasLength` validator is not working as expected when validating string/array lengths. When I pass a specific number to validate exact length, it's accepting values that are longer than the specified length. Similarly, the `min` option is rejecting values that should be valid.

### Reproduction

```js
import { hasLength } from '@mantine/form';

// Example 1: Exact length validation
const validator = hasLength(5);

// This should fail but passes
validator('hello world'); // length is 11, should only accept length 5

// Example 2: Min length validation
const minValidator = hasLength({ min: 3 });

// This should pass but fails
minValidator('abc'); // length is exactly 3, should be valid
```

### Expected behavior

- When passing a number directly to `hasLength(n)`, it should only accept values with **exact** length `n`
- When using `{ min: n }`, it should accept values with length **greater than or equal to** `n` (including exactly `n`)

### System Info
- @mantine/form version: latest
- Browser: Chrome

---
Repository: /testbed
