# Bug Report

### Describe the bug

I'm experiencing an issue with field validation behavior in forms. When I set `validateOnBlur` to `true`, the validation doesn't trigger when the field loses focus. Conversely, when I set it to `false`, validation unexpectedly runs on blur.

### Reproduction

```tsx
import { useField } from '@mantine/form';

// Case 1: validateOnBlur set to true
const field1 = useField({
  initialValue: '',
  validateOnBlur: true,
  validate: (value) => {
    console.log('Validation triggered');
    return value.length < 3 ? 'Too short' : null;
  }
});

// When field loses focus, validation doesn't run (but it should)
// Console doesn't show "Validation triggered"

// Case 2: validateOnBlur set to false
const field2 = useField({
  initialValue: '',
  validateOnBlur: false,
  validate: (value) => {
    console.log('Validation triggered');
    return value.length < 3 ? 'Too short' : null;
  }
});

// When field loses focus, validation runs (but it shouldn't)
// Console shows "Validation triggered"
```

### Expected behavior

When `validateOnBlur` is `true`, validation should trigger when the field loses focus (onBlur event).
When `validateOnBlur` is `false`, validation should NOT trigger on blur.

Currently, the behavior is inverted - it's doing the opposite of what's expected.

### System Info
- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
