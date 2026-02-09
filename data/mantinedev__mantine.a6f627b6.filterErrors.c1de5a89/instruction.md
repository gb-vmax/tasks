# Bug Report

### Describe the bug

When using form validation, empty string error messages are being included in the form errors object. This causes issues with error display logic since empty strings are truthy in JavaScript but shouldn't be treated as actual errors.

### Reproduction

```js
const form = useForm({
  initialValues: {
    email: '',
    username: ''
  },
  validate: {
    email: (value) => value ? null : '',
    username: (value) => value.length > 3 ? null : ''
  }
});

// After validation, errors object contains empty strings
form.validate();
// errors = { email: '', username: '' }

// These empty string errors are treated as actual errors
// even though they shouldn't be displayed
```

### Expected behavior

Empty string error messages should be filtered out from the errors object, similar to how `null`, `undefined`, and `false` values are already filtered. Only non-empty error messages should be included in the final errors object.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
