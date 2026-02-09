# Bug Report

### Describe the bug

The `DateInput` component no longer accepts custom `dateParser` functions. After a recent update, it appears that the `dateParser` prop has been changed from an optional function prop to a default implementation, which prevents users from providing their own parsing logic.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

// This custom parser is now ignored
const customParser = (value: string) => {
  // Custom logic to parse dates in a specific format
  const parts = value.split('-');
  if (parts.length === 3) {
    return new Date(parseInt(parts[2]), parseInt(parts[1]) - 1, parseInt(parts[0]));
  }
  return null;
};

function MyComponent() {
  return (
    <DateInput
      dateParser={customParser}  // This prop has no effect anymore
      label="Select date"
    />
  );
}
```

When trying to pass a custom `dateParser` function, it gets overridden by the internal implementation. The component always uses its built-in parsing logic regardless of what parser function is provided.

### Expected behavior

The `dateParser` prop should remain optional and allow users to provide custom date parsing functions. When a custom parser is provided, it should be used instead of the default implementation.

### System Info

- @mantine/dates version: latest
- React version: 18.x

This is breaking existing code that relies on custom date parsing logic for different locales or date formats. Would appreciate if this could be looked into!

---
Repository: /testbed
