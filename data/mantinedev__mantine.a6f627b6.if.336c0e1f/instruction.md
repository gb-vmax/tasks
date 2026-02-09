# Bug Report

### Describe the bug

I'm experiencing an issue with form inputs where setting a value to `null`, `undefined`, `0`, `false`, or an empty string doesn't work properly. The form field doesn't update when trying to clear it or set it to a falsy value.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    text: 'initial value',
    count: 5,
    enabled: true
  }
});

// These changes don't work as expected:
form.setFieldValue('text', ''); // Trying to clear the field
form.setFieldValue('count', 0); // Setting to zero
form.setFieldValue('enabled', false); // Setting to false
form.setFieldValue('text', null); // Setting to null
```

The form values remain unchanged when trying to set them to falsy values. This is problematic when trying to reset fields or set boolean flags to false.

### Expected behavior

The form should accept and properly handle falsy values including `null`, `undefined`, `0`, `false`, and empty strings. These are valid values that should be settable on form fields.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
