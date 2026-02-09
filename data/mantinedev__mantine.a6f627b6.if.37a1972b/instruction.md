# Bug Report

### Describe the bug

The `matchesField` validator is not working correctly when `values` is an empty object or falsy value. It's returning an error even when the field exists in the values object.

### Reproduction

```js
import { matchesField } from '@mantine/form';

const validator = matchesField('password', 'Passwords do not match');

// This incorrectly returns an error even though 'password' exists
const result = validator('test123', { password: 'test123' });
console.log(result); // Expected: null, Actual: 'Passwords do not match'

// Also fails with empty objects
const result2 = validator('test', {});
console.log(result2); // Expected: 'Passwords do not match', but behavior is inconsistent
```

### Expected behavior

The validator should:
1. Check if the field exists in the values object
2. Return `null` when the value matches the field
3. Return the error message when they don't match

Currently it's returning errors in cases where it shouldn't, making form validation fail unexpectedly.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
