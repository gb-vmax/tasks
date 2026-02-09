# Bug Report

### Describe the bug

The `matchesField` validator is not working correctly when the field being compared exists in the values object. It appears to be returning an error even when the field is present and should be validated.

### Reproduction

```js
import { matchesField } from '@mantine/form';

const validator = matchesField('password');

const values = {
  password: 'test123',
  confirmPassword: 'test123'
};

// This incorrectly returns an error even though 'password' field exists
const result = validator('test123', values);
console.log(result); // Expected: null, but returns error
```

### Expected behavior

When the field exists in the values object, the validator should proceed to compare the values. It should only return an error if:
1. The field doesn't exist in values, OR
2. The values don't match

In the example above, since both `password` and `confirmPassword` are 'test123', it should return `null` (no error).

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
