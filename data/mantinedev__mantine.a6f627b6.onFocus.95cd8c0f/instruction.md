# Bug Report

### Describe the bug

I'm experiencing an issue with the `useForm` hook where the `onFocus` handler is not being set correctly when using `getInputProps` with the `withFocus` option. Instead of setting the field as touched when focusing on an input, nothing happens on focus.

### Reproduction

```tsx
const form = useForm({
  initialValues: {
    email: '',
  },
});

// Using getInputProps with withFocus
<input {...form.getInputProps('email', { withFocus: true })} />
```

When I focus on the input field, the field is not marked as touched. The expected behavior is that focusing on the field should trigger the `onFocus` handler and set the field's touched state to `true`.

### Expected behavior

When focusing on an input field with `withFocus: true`, the field should be marked as touched via the `onFocus` handler. Currently, it seems like the `onFocus` handler is not being attached to the input props at all.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
