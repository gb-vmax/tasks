# Bug Report

### Describe the bug

I'm experiencing an issue with `DateInput` where dates are being parsed incorrectly when using the ISO format (YYYY-MM-DD). The day and month values appear to be swapped in the resulting date object.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

// When entering a date like "2024-03-15" (March 15, 2024)
// The component parses it as May 14, 2024 instead

<DateInput
  label="Date"
  placeholder="YYYY-MM-DD"
/>
```

Try entering `2024-03-15` in the input field. The expected result would be March 15, 2024, but the date object created has the month and day values switched around.

### Expected behavior

When entering a date string in ISO format (YYYY-MM-DD), the parser should correctly interpret:
- The first number as the year
- The second number as the month
- The third number as the day

So `2024-03-15` should be parsed as March 15, 2024, not May 14, 2024.

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox (occurs in both)

---
Repository: /testbed
