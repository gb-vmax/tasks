# Bug Report

### Describe the bug

Form validation is returning incorrect results - it's always showing `hasErrors: true` even when there are no validation errors. Additionally, the returned errors object contains unfiltered errors instead of the filtered ones.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: 'valid@email.com',
    name: 'John'
  },
  validate: {
    email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Invalid email'),
    name: (value) => (value.length > 0 ? null : 'Name required')
  }
});

// Validate with valid data
const result = form.validate();

console.log(result.hasErrors); // Expected: false, Actual: true
console.log(result.errors); // Contains unfiltered errors instead of filtered ones
```

### Expected behavior

When all validation rules pass:
- `hasErrors` should be `false`
- `errors` object should only contain actual validation errors (filtered)

When validation fails:
- `hasErrors` should be `true`  
- `errors` object should contain only the relevant validation errors

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
