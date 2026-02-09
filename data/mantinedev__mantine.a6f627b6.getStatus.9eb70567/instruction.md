# Bug Report

### Describe the bug

I'm experiencing an issue with form field status checking in nested form structures. When checking the status of a parent field, it's not correctly detecting the status of its child fields.

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
form.setFieldError('user.name', 'Name is required');

// This returns false even though user.name has an error
const hasError = form.getFieldStatus('user');
```

### Expected behavior

When a nested field like `user.name` has a status (error, touched, etc.), checking the parent field status `user` should return `true` to indicate that one or more of its child fields have that status.

Currently, the parent field status check doesn't seem to be picking up statuses from nested child fields properly.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
