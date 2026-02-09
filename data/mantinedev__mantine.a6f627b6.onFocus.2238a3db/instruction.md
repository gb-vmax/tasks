# Bug Report

### Describe the bug

When using `useForm` with the `withFocus` option, the field's touched state is not being set correctly on focus events. The field should be marked as touched when the user focuses on it, but this doesn't seem to be happening as expected.

### Reproduction

```jsx
const form = useForm({
  initialValues: {
    email: '',
  },
});

const inputProps = form.getInputProps('email', { withFocus: true });

// When the input is focused, the field should be marked as touched
// but checking form.isTouched('email') returns false
```

### Expected behavior

When a user focuses on an input field with `withFocus: true`, the field should be marked as touched (`form.isTouched('email')` should return `true`). This is important for validation flows where we want to show errors only after a user has interacted with a field.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
