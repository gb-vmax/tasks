# Bug Report

### Describe the bug

When using `useField` with `validateOnBlur` enabled, the validation is not triggering correctly on blur events. The field should validate when losing focus, but it appears the validation logic is inverted - it validates when it shouldn't and doesn't validate when it should.

### Reproduction

```tsx
import { useField } from '@mantine/form';

const field = useField({
  initialValue: '',
  validateOnBlur: true,
  validate: (value) => {
    if (!value) return 'Field is required';
    return null;
  }
});

// Steps:
// 1. Focus on the input field
// 2. Leave the field empty
// 3. Blur (click outside) the field
// Expected: Validation error should appear
// Actual: No validation occurs
```

### Expected behavior

When `validateOnBlur` is set to `true`, the field should validate when the blur event occurs. Currently, the validation doesn't run on blur even though the option is explicitly enabled.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
