# Bug Report

### Describe the bug

The `validateInputOnChange` option in forms appears to be working backwards. When I set `validateInputOnChange: true`, validation doesn't run on change, but when I set it to `false`, validation does run. The behavior is completely inverted from what's expected.

### Reproduction

```js
const form = useForm({
  initialValues: {
    email: '',
  },
  validate: {
    email: (value) => (!value.includes('@') ? 'Invalid email' : null),
  },
  validateInputOnChange: true, // Expecting validation on change
});

// Type into the email field - validation does NOT trigger
// But if I set validateInputOnChange: false, then validation DOES trigger
```

### Expected behavior

When `validateInputOnChange` is set to `true`, the form should validate the input as the user types. When set to `false`, validation should not occur on change (only on blur/submit).

Currently it's doing the opposite - `true` prevents validation on change, and `false` enables it.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
