# Bug Report

### Describe the bug

I'm experiencing an issue with form path handling in Mantine forms. When trying to access nested form values using dot notation paths, the form is not correctly parsing the path string. Instead of splitting the path by dots to access nested properties, it seems to be treating each character as a separate path segment.

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

// Trying to access nested value using path
form.getInputProps('user.profile.name');

// Expected: Should access form.values.user.profile.name
// Actual: Path is being split incorrectly, treating each character separately
```

When I try to use paths like `'user.profile.name'` to access nested form values, the behavior is completely broken. It looks like the path string is being split character by character instead of by the dot separator.

### Expected behavior

Form paths with dot notation (e.g., `'user.profile.name'`) should correctly navigate to nested properties in the form values object. The path should be split by `.` to create an array like `['user', 'profile', 'name']`.

### System Info
- @mantine/form version: latest
- React version: 18.x

This is making it impossible to work with nested form structures. Any help would be appreciated!

---
Repository: /testbed
