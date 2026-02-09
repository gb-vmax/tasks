# Bug Report

### Describe the bug

Form validation errors are not being filtered correctly when they contain empty strings. Empty string errors are being kept in the errors object instead of being removed, which causes validation error messages to display even when there's no actual error text.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
  },
  validate: {
    email: (value) => value.length < 2 ? '' : null,
  },
});

// After validation, the errors object contains:
// { email: '' }
// But it should be empty: {}
```

When a validation function returns an empty string, it's treated as an error even though there's no error message to display. This causes issues with conditional rendering based on whether errors exist.

### Expected behavior

Empty string error values should be filtered out from the errors object, similar to how `null`, `undefined`, and `false` values are currently filtered. The errors object should only contain actual error messages.

### System Info
- @mantine/form version: latest
- Framework: React

---
Repository: /testbed
