# Bug Report

### Describe the bug

The `matchesField` validator is not working correctly. It's supposed to validate that a field matches another field in the form, but it's returning validation errors even when the fields do match.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    password: '',
    confirmPassword: '',
  },
  validate: {
    confirmPassword: matchesField('password', 'Passwords do not match'),
  },
});

// Set both fields to the same value
form.setFieldValue('password', 'test123');
form.setFieldValue('confirmPassword', 'test123');

// Validation fails even though the fields match
form.validate();
// Expected: no errors
// Actual: validation error on confirmPassword
```

### Expected behavior

When both fields have the same value, the `matchesField` validator should pass and return no errors. The validator should only return an error when the fields don't match.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
