# Bug Report

### Describe the bug

I'm experiencing unexpected validation behavior with `validateInputOnChange` in Mantine forms. When I explicitly set `validateInputOnChange: false`, the form is actually validating on change instead of skipping validation. This is the opposite of what I expect.

### Reproduction

```jsx
import { useForm } from '@mantine/form';

const form = useForm({
  initialValues: {
    email: '',
  },
  validateInputOnChange: false, // Trying to disable validation on change
  validate: {
    email: (value) => (value.includes('@') ? null : 'Invalid email'),
  },
});

// When typing in the email input, validation runs on every keystroke
// even though validateInputOnChange is set to false
```

### Expected behavior

When `validateInputOnChange` is set to `false`, the form should NOT validate inputs as the user types. Validation should only occur on form submission or when explicitly triggered. Currently it seems like the setting is being inverted - `false` enables validation and `true` (or omitting the prop) disables it.

### System Info
- @mantine/form version: latest
- React version: 18.x
- Browser: Firefox/Chrome

This is really confusing because the behavior is backwards from what the prop name suggests. Is this a known issue?

---
Repository: /testbed
