# Bug Report

### Describe the bug

Form validation is triggering on every change even when `validateInputOnChange` is set to `false`. The validation should only run when explicitly enabled, but it seems to be ignoring the configuration and validating on all input changes.

### Reproduction

```js
const form = useForm({
  initialValues: {
    email: ''
  },
  validate: {
    email: (value) => (value.includes('@') ? null : 'Invalid email')
  },
  validateInputOnChange: false
});

// Type in the input field
// Validation runs on every keystroke even though validateInputOnChange is false
```

### Expected behavior

When `validateInputOnChange` is set to `false`, the form should not validate fields on change. Validation should only occur on blur or form submission, not on every input change.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
