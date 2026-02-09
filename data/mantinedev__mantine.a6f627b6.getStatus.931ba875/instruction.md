# Bug Report

### Describe the bug

I'm experiencing an issue with form field status checking. When I have nested form fields and try to check their validation/error status, it's not working as expected. The status check always returns `false` even when there are actual errors on the nested fields.

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

// This returns false, but should return true
const hasError = form.getStatus('user');
```

### Expected behavior

When a nested field like `user.name` has an error, checking the status of the parent path `user` should return `true` to indicate that there are errors in that section of the form.

This is particularly problematic when trying to show error indicators on form sections or accordion panels that contain multiple fields.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
