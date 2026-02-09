# Bug Report

### Describe the bug

I'm experiencing an issue with the `useField` hook where error messages aren't being displayed correctly. It seems like the error resolver isn't being used at all, so when validation errors occur, they're not showing up in the UI as expected.

### Reproduction

```tsx
import { useField } from '@mantine/form';

function MyComponent() {
  const field = useField({
    initialValue: '',
    validate: (value) => {
      if (!value) {
        return 'This field is required';
      }
      return null;
    }
  });

  // After validation fails, field.error is not rendered properly
  return (
    <div>
      <input {...field.getInputProps()} />
      {field.error && <div className="error">{field.error}</div>}
    </div>
  );
}
```

### Expected behavior

When validation fails, the error message should be properly resolved and displayed. The hook should handle different error formats (strings, arrays, objects with message property, etc.) and convert them to displayable React nodes.

### Additional context

This seems to have broken recently. The error resolver function exists in the code but it's not being connected to the actual field implementation, so errors are either not displayed or displayed in their raw format instead of being properly formatted.

---
Repository: /testbed
