# Bug Report

### Describe the bug

I'm experiencing an issue with form values in uncontrolled mode. After calling `setValues()`, the form's internal state becomes corrupted and subsequent operations fail with type errors. It seems like the reference to the form values is being set to something unexpected instead of the actual values object.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  mode: 'uncontrolled',
  initialValues: {
    name: 'John',
    email: 'john@example.com'
  }
});

// Update form values
form.setValues({ name: 'Jane', email: 'jane@example.com' });

// Try to access values - this breaks
console.log(form.values); // Expected object, but getting something else
```

After calling `setValues`, the form state seems to be pointing to the wrong reference. Any subsequent operations that try to read or update form values fail because `values` is no longer the expected object structure.

### Expected behavior

When using `setValues()` in uncontrolled mode, the form's values should be properly updated and remain accessible as a normal object. The internal reference should point to the updated values object, not to something else.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
