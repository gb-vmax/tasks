# Bug Report

### Describe the bug

When using form inputs with `getInputOnChange`, checkbox inputs are not working correctly. The value is not being set when checking/unchecking a checkbox input field.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    termsAccepted: false,
  },
});

// Checkbox input
<input
  type="checkbox"
  {...form.getInputProps('termsAccepted')}
/>

// Checking the checkbox doesn't update the form value
// form.values.termsAccepted remains false
```

### Expected behavior

When a checkbox is checked or unchecked, the form value should update accordingly. The checkbox state should be properly captured and the form should reflect the checked/unchecked state.

### System Info
- @mantine/form version: latest
- Browser: Chrome 120

---
Repository: /testbed
