# Bug Report

### Describe the bug

The `matchesField` validator is not working correctly - it's returning an error even when the field values match. It seems like the validation logic is inverted, causing fields that should pass validation to fail instead.

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

// Validation fails even though the values match
form.validate();
// confirmPassword field shows error: "Passwords do not match"
```

### Expected behavior

When both fields have the same value, the `matchesField` validator should return `null` (no error). The validation should only fail when the values are different.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
