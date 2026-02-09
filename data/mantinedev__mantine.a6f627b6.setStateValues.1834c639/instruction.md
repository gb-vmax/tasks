# Bug Report

### Describe the bug

I'm experiencing an issue with form state management in controlled mode. When updating form values programmatically using `setValues()`, the internal reference values are not being synchronized correctly with the state values in controlled mode.

### Reproduction

```js
const form = useForm({
  mode: 'controlled',
  initialValues: {
    name: 'John',
    email: 'john@example.com'
  }
});

// Update values programmatically
form.setValues({ name: 'Jane', email: 'jane@example.com' });

// The form state appears inconsistent - internal refs don't match the actual state
```

### Expected behavior

In controlled mode, when `setValues()` is called, the internal reference values should properly reflect the current state values. The form should maintain consistency between its internal state tracking and the actual form values.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
