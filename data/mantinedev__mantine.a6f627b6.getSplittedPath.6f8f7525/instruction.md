# Bug Report

### Describe the bug

I'm experiencing an issue with form field paths not being parsed correctly. When I try to access nested form values using dot notation paths like `'user.profile.name'`, the form doesn't seem to recognize the path structure properly.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    user: {
      profile: {
        name: 'John'
      }
    }
  }
});

// Trying to access nested field
form.getInputProps('user.profile.name');
// Expected: Should work with the nested path
// Actual: Path doesn't seem to be parsed correctly
```

### Expected behavior

The form should properly parse dot-notation paths and allow access to deeply nested fields. For example, `'user.profile.name'` should be split into `['user', 'profile', 'name']` to traverse the object structure.

### System Info
- @mantine/form version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
