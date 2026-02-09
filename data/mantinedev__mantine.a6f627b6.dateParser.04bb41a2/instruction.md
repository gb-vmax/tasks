# Bug Report

### Describe the bug

The `DateInput` component is not accepting custom `dateParser` functions anymore. When I try to pass my own parser function, I get a TypeScript error saying that the property is not assignable.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

function MyComponent() {
  const customParser = (value: string) => {
    // Custom parsing logic
    if (!value) return null;
    return new Date(value);
  };

  return (
    <DateInput
      dateParser={customParser}  // TypeScript error here
      label="Select date"
    />
  );
}
```

### Expected behavior

Should be able to pass a custom `dateParser` function to override the default parsing behavior. This was working in previous versions.

### System Info

- @mantine/dates version: latest
- TypeScript version: 5.x
- React version: 18.x

---
Repository: /testbed
