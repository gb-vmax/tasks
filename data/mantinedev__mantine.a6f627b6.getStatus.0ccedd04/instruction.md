# Bug Report

### Describe the bug

I'm experiencing an issue with form field status checking where the status is not being correctly detected for nested field paths. When I check the status of a parent field, it's not properly considering the status of its nested children.

### Reproduction

```js
const form = useForm({
  initialValues: {
    user: {
      name: '',
      email: ''
    }
  }
});

// Set error on nested field
form.setFieldError('user.name', 'Required');

// Check parent status - returns incorrect result
const hasError = form.isValid('user'); // Should detect nested error but doesn't
```

Also noticed that when checking status for fields like `user.name`, it incorrectly matches paths like `username` because it's checking for prefix match without the dot separator.

### Expected behavior

- When checking status for a parent path (e.g., `user`), it should correctly detect if any nested child paths (e.g., `user.name`, `user.email`) have that status
- Path matching should be exact and not match unrelated fields that happen to start with the same characters

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
