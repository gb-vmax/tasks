# Bug Report

### Describe the bug

When using form inputs with `getInputOnChange`, passing boolean values (specifically `false`) to the onChange handler doesn't work correctly. The value is not being set as expected.

### Reproduction

```js
const form = useForm({
  initialValues: {
    isEnabled: true
  }
});

// When trying to set a boolean false value
const handleChange = getInputOnChange(form.setFieldValue('isEnabled'));
handleChange(false); // This doesn't set the value to false
```

The issue occurs when trying to set a falsy value like `false` or `0`. The form field doesn't update to the new value.

### Expected behavior

The form should accept and properly set falsy boolean values like `false`, as well as numeric values like `0`. These are valid values that should be handled correctly by the onChange handler.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
