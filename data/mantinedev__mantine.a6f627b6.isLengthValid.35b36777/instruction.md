# Bug Report

### Describe the bug

The `hasLength` validator is not working as expected. When I specify an exact length requirement using a number, it accepts values that are longer than the required length. Similarly, when using the `max` option, it's rejecting values that should be valid.

### Reproduction

```js
import { hasLength } from '@mantine/form';

// Case 1: Exact length validation
const validator = hasLength(5);

// This should fail but passes
validator('hello world'); // length is 11, should only accept length 5

// Case 2: Max length validation  
const maxValidator = hasLength({ max: 10 });

// This should pass but fails
maxValidator('exactly10'); // length is 9, should be valid with max 10
```

### Expected behavior

1. When passing a number to `hasLength(n)`, it should only accept values with **exactly** length `n`
2. When using `{ max: n }`, it should accept values with length **less than or equal to** `n`, not less than `n`

This is causing form validation to behave incorrectly in my application - users can submit inputs that exceed the intended length limits, and valid inputs are being rejected.

### System Info
- @mantine/form version: latest
- Browser: Chrome

---
Repository: /testbed
