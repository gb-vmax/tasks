# Bug Report

### Describe the bug

I'm experiencing an issue with checkbox inputs in forms where the value handling seems to be inverted. When I check a checkbox, it's setting the value to the text content instead of the checked state, and text inputs are being treated like checkboxes.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    acceptTerms: false,
    username: ''
  }
});

// When checking a checkbox:
// Expected: form.values.acceptTerms should be true
// Actual: form.values.acceptTerms gets set to some string value

// When typing in a text input:
// Expected: form.values.username should be the typed text
// Actual: Seems to be checking for a 'checked' property that doesn't exist
```

### Steps to reproduce

1. Create a form with a checkbox input bound to the form
2. Check the checkbox
3. The value is not correctly set to the checked state
4. Similarly, text inputs don't update properly

### Expected behavior

- Checkbox inputs should set the form value to `true`/`false` based on the `checked` property
- Text inputs (including textarea and select) should set the form value to the input's `value` property

This seems like the logic for handling different input types got mixed up somehow. The checkbox handling and regular input handling appear to be swapped.

### System Info

- @mantine/form version: latest
- Browser: Chrome

---
Repository: /testbed
