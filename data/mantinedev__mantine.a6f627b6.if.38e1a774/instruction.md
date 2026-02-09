# Bug Report

### Describe the bug

I'm experiencing an issue with the `matchesField` validator where it's not properly validating when the field value doesn't match. The validator seems to be returning errors in cases where it shouldn't, particularly when the values object exists but the field doesn't match.

### Reproduction

```js
import { matchesField } from '@mantine/form';

const validator = matchesField('password', 'Passwords do not match');

const values = {
  password: 'test123',
  confirmPassword: 'test123'
};

// This should return null (no error) since passwords match
// But the validator is not working as expected
const result = validator('test123', values);
```

### Expected behavior

When the field values match, the validator should return `null` (no error). The validator should only return an error when:
1. The values are actually different
2. The field doesn't exist in the values object

Currently it seems like the validation logic is inverted or broken in some way.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
