# Bug Report

### Describe the bug

The `onBlur` validation is not triggering correctly in form fields. When `validateOnBlur` is set to `true`, the field validation doesn't run when the input loses focus. It seems like the validation logic is inverted - fields validate when they shouldn't and don't validate when they should.

### Reproduction

```js
const field = useField({
  initialValue: '',
  validateOnBlur: true,
  validate: (value) => {
    if (!value) return 'Field is required';
    return null;
  }
});

// Steps:
// 1. Focus on the input field
// 2. Leave the field empty
// 3. Blur the input (click outside)
// Expected: Validation should run and show error
// Actual: No validation occurs
```

Also happens in reverse - when `validateOnBlur` is set to `false`, validation runs on blur even though it shouldn't.

### Expected behavior

- When `validateOnBlur` is `true`, validation should run when the field loses focus
- When `validateOnBlur` is `false`, validation should NOT run on blur

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
