# Bug Report

### Describe the bug

When using `useField` with `withFocus` option enabled, the focus event handler is not being attached to the field. The field should mark itself as touched when focused, but nothing happens when I focus on the input.

### Reproduction

```jsx
const field = useField({
  initialValue: '',
  withFocus: true,
});

// Focus event handler is missing from the returned payload
console.log(field.getInputProps()); // onFocus is undefined
```

Steps to reproduce:
1. Create a field with `useField` and set `withFocus: true`
2. Get the input props using `getInputProps()`
3. Try to focus the input element
4. The field doesn't get marked as touched

### Expected behavior

When `withFocus` is enabled, the field should:
- Have an `onFocus` handler attached to the input props
- Mark the field as touched when the input receives focus
- Work consistently regardless of whether an `onFocus` handler already exists

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
