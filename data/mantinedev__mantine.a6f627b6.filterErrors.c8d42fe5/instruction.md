# Bug Report

### Describe the bug

Form error filtering is not working as expected. When I set form errors, they're not being displayed properly. It seems like the error filtering logic is inverted - errors that should be shown are being filtered out, and invalid values that should be filtered are being kept.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
    username: '',
  },
});

// Set some validation errors
form.setErrors({
  email: 'Invalid email',
  username: null,  // This should be filtered out
  password: false, // This should also be filtered out
});

// Expected: Only 'email' error should be present
// Actual: No errors are shown, or wrong errors are kept
console.log(form.errors);
```

### Expected behavior

- Valid error messages (strings) should be kept and displayed
- `null`, `undefined`, and `false` values should be filtered out from the errors object
- The form should only show actual error messages to the user

### Current behavior

The error filtering appears to be backwards - either no errors are shown when they should be, or invalid error values (null/false) are being kept instead of filtered out.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
