# Bug Report

### Describe the bug

When using date range picker, the date formatting is broken. If I select only the start date (first date in the range), nothing gets displayed in the input field. The input stays empty even though a date has been selected.

### Reproduction

```js
import { DatePickerInput } from '@mantine/dates';

// Set up a range picker
<DatePickerInput
  type="range"
  placeholder="Pick date range"
/>

// Steps:
// 1. Click on the input to open the calendar
// 2. Select a start date (first date)
// 3. Don't select an end date yet
// 4. The input field remains empty instead of showing the selected start date
```

### Expected behavior

When selecting the first date in a range, the input should display the start date followed by the separator (e.g., "12/01/2024 – "). Currently, the input stays completely empty until both dates are selected.

Also noticed that when `type="multiple"` is used with a `null` value, it throws an error trying to call `.map()` on null.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
