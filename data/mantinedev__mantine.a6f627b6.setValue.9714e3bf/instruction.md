# Bug Report

### Describe the bug

When using form inputs with checkboxes, the checked state appears to be inverted. Clicking a checkbox sets it to the opposite state of what's expected - checking the box results in `false` being stored, and unchecking it stores `true`.

### Reproduction

```js
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    acceptTerms: false
  }
});

// When user clicks checkbox to check it:
// Expected: acceptTerms becomes true
// Actual: acceptTerms becomes false

// When user clicks checkbox to uncheck it:
// Expected: acceptTerms becomes false  
// Actual: acceptTerms becomes true
```

### Steps to reproduce:
1. Create a form with a checkbox field
2. Set initial value to `false`
3. Click the checkbox to check it
4. Observe that the form value is `false` instead of `true`

### Expected behavior

Checking a checkbox should set the form value to `true`, and unchecking it should set it to `false`.

### System Info
- @mantine/form version: latest
- React version: 18.x

This is causing issues in our forms where we need to validate that users have accepted terms and conditions before submitting.

---
Repository: /testbed
