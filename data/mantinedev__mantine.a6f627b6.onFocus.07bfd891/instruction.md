# Bug Report

### Describe the bug

When using `useField` with `withFocus` option enabled, the `onFocus` event handler is now setting the `touched` state asynchronously, which causes the touched state to not be immediately available when needed. This breaks scenarios where you need to check if a field has been touched right after focusing on it.

### Reproduction

```jsx
const field = useField({
  initialValue: '',
  withFocus: true,
});

// Focus on the field
field.getInputProps().onFocus();

// Try to check touched state immediately
console.log(field.isTouched()); // Returns false, but should be true
```

### Expected behavior

The `touched` state should be set synchronously when the field receives focus, so that `isTouched()` returns `true` immediately after calling `onFocus()`. The current implementation wraps `setTouched(true)` in a `Promise.resolve().then()`, which delays the state update and makes it unavailable for synchronous checks.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
