# Bug Report

### Describe the bug

When using the months list in date picker components, the month names are not being matched correctly. It seems like extra whitespace or empty text content from buttons is interfering with the month name comparison.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

function Demo() {
  return (
    <MonthsList
      month={new Date(2024, 0)}
      locale="en"
    />
  );
}
```

When the component renders, the month names extracted from the buttons include extra whitespace or empty strings, causing validation to fail when comparing against the expected month names array.

### Expected behavior

The month names should be extracted cleanly without any extra whitespace or empty button text content. The comparison should match the expected array of month names exactly.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
