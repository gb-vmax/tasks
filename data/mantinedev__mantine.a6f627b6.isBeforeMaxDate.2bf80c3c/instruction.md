# Bug Report

### Describe the bug

The date picker is not respecting the `maxDate` prop correctly. Dates that should be selectable (before the max date) are being disabled, while dates after the max date are being allowed.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function App() {
  return (
    <DatePicker
      maxDate={new Date(2024, 0, 15)} // January 15, 2024
    />
  );
}
```

When clicking on the date picker:
- Dates before January 15, 2024 are disabled (they shouldn't be)
- Dates after January 15, 2024 can be selected (they shouldn't be)

The behavior seems completely inverted from what's expected.

### Expected behavior

Dates before and including the `maxDate` should be selectable, while dates after `maxDate` should be disabled.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
