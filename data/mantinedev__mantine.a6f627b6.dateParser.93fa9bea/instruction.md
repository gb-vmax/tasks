# Bug Report

### Describe the bug

The `DateInput` component no longer accepts a custom `dateParser` prop. It seems like the ability to provide a custom date parsing function has been removed, which breaks existing code that relies on custom date parsing logic.

### Reproduction

```tsx
import { DateInput } from '@mantine/dates';

// Custom parser for specific date format
const customParser = (value: string) => {
  // Custom logic for parsing dates in DD-MM-YYYY format
  const parts = value.split('-');
  if (parts.length === 3) {
    return new Date(parseInt(parts[2]), parseInt(parts[1]) - 1, parseInt(parts[0]));
  }
  return null;
};

// This no longer works - dateParser prop is not recognized
<DateInput
  dateParser={customParser}
  placeholder="Enter date"
/>
```

### Expected behavior

The component should accept a `dateParser` prop as a function that allows users to provide their own date parsing logic. This was working in previous versions and is documented in the API.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
