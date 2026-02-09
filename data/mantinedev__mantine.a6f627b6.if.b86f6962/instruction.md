# Bug Report

### Describe the bug

I'm experiencing an issue with form inputs where passing `null` or `undefined` values to `onChange` handlers doesn't work correctly. When trying to clear a field by setting it to `null` or `undefined`, the value doesn't update as expected.

### Reproduction

```js
const form = useForm({
  initialValues: {
    name: 'John Doe'
  }
});

// This doesn't clear the field as expected
form.getInputProps('name').onChange(null);

// Also doesn't work with undefined
form.getInputProps('name').onChange(undefined);
```

### Expected behavior

When passing `null` or `undefined` to the `onChange` handler, the form field should be cleared/reset. The field value should be set to the provided falsy value.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
