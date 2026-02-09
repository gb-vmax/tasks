# Bug Report

### Describe the bug

When using `useField` with the `withFocus` option enabled, the field's touched state is being set incorrectly on focus. The field is marked as untouched when focused, which is the opposite of the expected behavior.

### Reproduction

```jsx
const { getInputProps } = useField({
  initialValue: '',
  withFocus: true,
});

const inputProps = getInputProps();

// Focus the input
inputProps.onFocus();

// Expected: field should be marked as touched
// Actual: field is marked as untouched (touched = false)
```

### Expected behavior

When a field receives focus with `withFocus: true`, it should be marked as touched (`setTouched(true)`), not untouched. This is important for form validation and showing error states after user interaction.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
