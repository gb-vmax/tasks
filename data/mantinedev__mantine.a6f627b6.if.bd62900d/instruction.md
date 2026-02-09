# Bug Report

### Describe the bug

When using form inputs with boolean values, setting the value to `false` doesn't work correctly. The form field doesn't update when trying to set a boolean `false` value, but setting it to `true` works fine.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    isActive: true
  }
});

// This doesn't work - the field stays true
form.setFieldValue('isActive', false);

// This works fine
form.setFieldValue('isActive', true);
```

The issue seems to be that `false` is treated as a falsy value and gets handled incorrectly. When I try to toggle a boolean field from `true` to `false`, the value doesn't update in the form state.

### Expected behavior

Setting a form field to `false` should work the same way as setting it to `true` or any other valid value. Boolean `false` is a legitimate value and should be handled correctly.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
