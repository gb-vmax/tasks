# Bug Report

### Describe the bug

The `TimeValue` component is displaying incorrect AM/PM labels and hour values when formatting times in 12-hour format. Specifically, 12:00 PM (noon) is being shown as 12:00 AM, and the PM period is not being applied correctly for hours between 12-23.

### Reproduction

```js
import { getFormattedTime } from '@mantine/dates';

// Test case 1: Noon should be 12:00 PM, but shows as 12:00 AM
const noon = getFormattedTime({
  value: '12:00',
  format: '12',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
console.log(noon); // Expected: "12:00 PM", Actual: "12:00 AM"

// Test case 2: 1 PM should show as 1:00 PM
const onePm = getFormattedTime({
  value: '13:00',
  format: '12',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
console.log(onePm); // Expected: "1:00 PM", but may show incorrect value

// Test case 3: Midnight should be 12:00 AM
const midnight = getFormattedTime({
  value: '00:00',
  format: '12',
  amPmLabels: { am: 'AM', pm: 'PM' }
});
console.log(midnight); // Expected: "12:00 AM"
```

### Expected behavior

- 00:00 (midnight) should display as "12:00 AM"
- 12:00 (noon) should display as "12:00 PM"
- Hours 13-23 should correctly convert to 1-11 PM
- The AM/PM label should correctly reflect morning (00:00-11:59) vs afternoon/evening (12:00-23:59)

### System Info

- @mantine/dates version: latest
- Browser: All browsers affected

---
Repository: /testbed
