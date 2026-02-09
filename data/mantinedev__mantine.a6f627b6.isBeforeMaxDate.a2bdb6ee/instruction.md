# Bug Report

### Describe the bug

The `maxDate` property in date picker components is not working correctly. When I set a `maxDate`, dates that should be selectable (including the max date itself) are being disabled. It seems like the boundary check is too strict and is excluding the maximum date from the valid range.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

// Setting maxDate to a specific date
<DatePicker 
  maxDate={new Date('2024-01-15')}
/>
```

When I try to select January 15th, 2024 (the maxDate), it's disabled even though it should be selectable. The component seems to be treating the maxDate as exclusive rather than inclusive.

### Expected behavior

The date specified in `maxDate` should be selectable. If I set `maxDate` to January 15th, I should be able to select any date up to and including January 15th. Currently, it appears that only dates before the maxDate are selectable, but not the maxDate itself.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
