# Bug Report

### Describe the bug

I'm experiencing an infinite loop/crash when using `useField` with certain error objects. The application becomes unresponsive and the browser tab freezes.

### Reproduction

```js
const field = useField({
  initialValue: '',
  validate: (value) => {
    if (!value) {
      // Returning a circular reference or complex error object
      const error = { message: 'Required field' };
      error.nested = error; // circular reference
      return error;
    }
  }
});
```

When the validation runs with this type of error object, the app hangs completely.

### Expected behavior

The error should be displayed properly without causing the application to freeze. Even with complex or circular error structures, the field should handle it gracefully and show some error message.

### System Info
- @mantine/form version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
