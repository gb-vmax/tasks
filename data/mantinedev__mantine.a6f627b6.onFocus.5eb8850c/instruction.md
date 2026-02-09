# Bug Report

### Describe the bug

When using `useForm` with `withFocus` enabled, the field touched state is being set incorrectly on focus. Instead of immediately marking a field as touched when it receives focus, the field is first marked as untouched and then marked as touched after a delay.

This causes issues with validation timing and can lead to unexpected behavior where:
1. Fields appear untouched momentarily when focused
2. Validation states may flash or update incorrectly
3. The touched state doesn't reflect the actual user interaction

### Reproduction

```tsx
const form = useForm({
  initialValues: {
    email: '',
  },
});

// Get input props with withFocus enabled
const inputProps = form.getInputProps('email', { withFocus: true });

// When the input is focused, the field is first set to untouched (false)
// then set to touched (true) after a setTimeout
// This causes a brief moment where the field appears untouched
```

### Expected behavior

When a field receives focus with `withFocus` enabled, it should immediately be marked as touched without any delay or intermediate state changes. The `onFocus` handler should directly set the field's touched state to `true` without first setting it to `false`.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
