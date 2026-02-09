# Bug Report

### Describe the bug

When using form inputs with boolean values, setting a field to `false` doesn't work correctly. The form treats `false` as a falsy value and doesn't update the field properly. This affects checkboxes and any other inputs that need to store boolean `false` values.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    isEnabled: true,
  },
});

// Try to set the value to false
form.setFieldValue('isEnabled', false);

// The value doesn't update correctly because false is treated as falsy
console.log(form.values.isEnabled); // Expected: false, but doesn't work as expected
```

### Expected behavior

The form should correctly handle `false` as a valid boolean value and update the field. Boolean `false` should be treated differently from `null` or `undefined`.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
