# Bug Report

### Describe the bug

When using form validation, empty string errors (`''`) are now being included in the form errors object. This causes forms to be considered invalid even when errors are cleared or set to empty strings.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
  },
});

// Set an error to empty string (e.g., when clearing validation)
form.setFieldError('email', '');

// The error is still present in the errors object
console.log(form.errors); // { email: '' }

// Form is considered invalid even though the error is an empty string
console.log(form.isValid()); // false
```

### Expected behavior

Empty string errors should be filtered out from the errors object, similar to how `null`, `undefined`, and `false` values are filtered. When an error is set to an empty string, it should be treated as "no error" and removed from the errors object.

```js
// Expected output
console.log(form.errors); // {}
console.log(form.isValid()); // true
```

This is particularly problematic when dynamically clearing errors or when validation functions return empty strings to indicate no error.

### System Info
- @mantine/form version: latest
- Browser: Chrome

---
Repository: /testbed
