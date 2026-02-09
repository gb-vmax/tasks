# Bug Report

### Describe the bug

I'm experiencing an issue with form path handling where accessing nested form fields using dot notation paths is completely broken. When trying to use string paths like `'user.name'` or `'profile.settings.email'` to access nested form values, the form system doesn't work at all.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    user: {
      name: 'John',
      email: 'john@example.com'
    }
  }
});

// Trying to access nested field with path
form.getInputProps('user.name'); // Doesn't work
form.setFieldValue('user.email', 'newemail@example.com'); // Doesn't update the field
```

### Expected behavior

String paths with dot notation should be properly parsed to access nested object properties in the form. For example, `'user.name'` should split into `['user', 'name']` to traverse the form values object.

### System Info

- @mantine/form version: latest
- React version: 18.x
- Browser: Chrome

This seems to have broken recently, as nested field paths were working fine before. Any path-based form operations are now completely non-functional.

---
Repository: /testbed
