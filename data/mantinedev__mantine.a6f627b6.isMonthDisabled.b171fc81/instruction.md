# Bug Report

### Describe the bug

The `MonthsList` component is not correctly disabling months based on `minDate` and `maxDate` props. Months that should be selectable are being disabled, and months that should be disabled are selectable.

### Reproduction

```jsx
import { MonthsList } from '@mantine/dates';

// Set minDate to January 2023
const minDate = new Date(2023, 0, 1);

// Months before January 2023 should be disabled, but instead
// months AFTER January 2023 are being disabled
<MonthsList minDate={minDate} />

// Similarly with maxDate
const maxDate = new Date(2023, 11, 31);

// Months after December 2023 should be disabled, but the behavior is incorrect
<MonthsList maxDate={maxDate} />
```

### Expected behavior

- When `minDate` is set, all months **before** that date should be disabled
- When `maxDate` is set, all months **after** that date should be disabled
- Months within the valid range should be selectable

### Current behavior

The logic appears to be inverted - months that should be enabled are disabled and vice versa. This makes it impossible to properly restrict month selection in date pickers.

---
Repository: /testbed
