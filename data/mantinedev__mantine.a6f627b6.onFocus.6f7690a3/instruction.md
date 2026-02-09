# Bug Report

### Describe the bug

When using `useField` with `withFocus` enabled, the field is not being marked as touched when the user focuses on it. The `onFocus` handler appears to check if the field is already touched before setting it to touched, which prevents the field from ever being marked as touched on focus.

### Reproduction

```tsx
import { useField } from '@mantine/form';

function MyComponent() {
  const field = useField({
    initialValue: '',
    withFocus: true,
  });

  // Focus the input
  // Expected: field should be marked as touched
  // Actual: field remains untouched

  return (
    <div>
      <input {...field.getInputProps()} />
      <p>Touched: {field.isTouched() ? 'Yes' : 'No'}</p>
    </div>
  );
}
```

### Expected behavior

When a user focuses on an input field with `withFocus: true`, the field should be marked as touched immediately. The touched state should change from `false` to `true` on the first focus event.

### System Info

- @mantine/form version: latest
- React version: 18.x

---
Repository: /testbed
