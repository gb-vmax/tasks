# Bug Report

### Describe the bug

I'm experiencing an issue with form validation errors not being displayed correctly. When I set validation errors on my form fields, they're not showing up in the UI even though the validation is running.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
    name: ''
  }
});

// Set errors manually
form.setErrors({
  email: 'Invalid email',
  name: 'Name is required'
});

// The errors object is empty even though we just set errors
console.log(form.errors); // Expected: { email: 'Invalid email', name: 'Name is required' }
                          // Actual: {}
```

### Expected behavior

When setting form errors, they should be visible in the form's error state and displayed in the UI. The `form.errors` object should contain the error messages that were set.

### System Info

- @mantine/form version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
