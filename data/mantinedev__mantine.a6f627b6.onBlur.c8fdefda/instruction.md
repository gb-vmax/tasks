# Bug Report

### Describe the bug

Field validation is not triggering correctly on blur events. When I set up a field with `validateOnBlur` option, the validation doesn't run when the field loses focus. It seems like the blur handler is checking the wrong validation mode.

### Reproduction

```tsx
const field = useField({
  initialValue: '',
  validateOnBlur: true,
  validate: (value) => {
    if (!value) return 'Field is required';
    return null;
  }
});

// When the input loses focus, validation should run but it doesn't
<input
  {...field.getInputProps()}
  onBlur={field.onBlur}
/>
```

### Expected behavior

When `validateOnBlur` is set to `true`, the field should validate when it loses focus (onBlur event). Currently, the validation is not being triggered at all on blur.

### Additional context

This seems to have broken recently. The blur validation was working fine in previous versions but now it's completely not responding to blur events.

---
Repository: /testbed
