# Bug Report

### Describe the bug

I'm experiencing an issue with form field status checking when working with nested field paths. The `getStatus` function seems to be returning incorrect results for fields that have similar path prefixes.

### Reproduction

```js
const form = useForm({
  initialValues: {
    user: '',
    username: ''
  }
});

// Set error on 'user' field
form.setFieldError('user', 'Required');

// This incorrectly returns true even though 'username' has no error
const hasUsernameError = form.getFieldStatus('username');
```

The problem occurs when checking the status of a field whose path is a prefix of another field's path. For example, if I have errors on `user` and check the status of `username`, it returns `true` even though `username` itself has no errors.

### Expected behavior

`getFieldStatus('username')` should return `false` when only `user` has an error. The status check should only match the exact field path or its actual nested children (e.g., `user.profile`), not fields that just happen to start with the same characters.

### Additional context

This seems to affect any field name that shares a prefix with another field. Other examples:
- `address` vs `addressLine2`
- `email` vs `emailConfirm`
- `name` vs `names`

---
Repository: /testbed
