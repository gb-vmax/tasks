# Bug Report

### Describe the bug

Form validation is not working correctly - the `hasErrors` flag is inverted and filtered errors are not being returned properly. When a form has validation errors, `hasErrors` is reported as `false`, and when there are no errors, it's reported as `true`. Additionally, the unfiltered errors object is being returned instead of the filtered one.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
    name: ''
  },
  validate: {
    email: (value) => (value.length < 1 ? 'Email is required' : null),
    name: (value) => (value.length < 1 ? 'Name is required' : null)
  }
});

// Validate empty form
const result = form.validate();

console.log(result.hasErrors); // Expected: true, Actual: false
console.log(result.errors); // Contains unfiltered errors instead of filtered ones
```

### Expected behavior

1. When validation fails, `hasErrors` should be `true`
2. When validation passes, `hasErrors` should be `false`
3. The returned errors object should contain only the filtered/relevant errors

### System Info
- @mantine/form version: latest
- Browser: Chrome

This seems like a regression that breaks form validation logic completely. Any form relying on the `hasErrors` flag will behave incorrectly.

---
Repository: /testbed
