# Bug Report

### Describe the bug

The `maxDate` prop in the DatePicker/Month component is not working correctly. Dates that should be disabled (after the max date) are being allowed, and dates that should be selectable (before/equal to the max date) are being disabled instead.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

// Set maxDate to December 31, 2023
<DatePicker maxDate={new Date(2023, 11, 31)} />
```

When using the component:
1. Dates before December 31, 2023 are disabled (they shouldn't be)
2. Dates after December 31, 2023 are selectable (they should be disabled)
3. The behavior is completely inverted from what's expected

### Expected behavior

- Dates on or before `maxDate` should be selectable
- Dates after `maxDate` should be disabled
- For example, with `maxDate` set to December 31, 2023:
  - December 30, 2023 → should be selectable ✓
  - December 31, 2023 → should be selectable ✓
  - January 1, 2024 → should be disabled ✓

### System Info

- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
