# Bug Report

### Describe the bug

The `DateInput` component is not properly validating dates when a `minDate` is set. Dates that should be considered valid (i.e., dates that are equal to or after `minDate`) are being rejected as invalid.

### Reproduction

```js
import { DateInput } from '@mantine/dates';

// Set minDate to January 15, 2024
const minDate = new Date(2024, 0, 15);

// Try to select January 15, 2024 (the same date as minDate)
// Expected: Should be valid
// Actual: Gets rejected as invalid

<DateInput
  minDate={minDate}
  value={new Date(2024, 0, 15)}
/>
```

### Expected behavior

When `minDate` is set, the component should accept:
- Dates equal to `minDate` 
- Dates after `minDate`

Currently, it seems like dates equal to `minDate` are being treated as invalid, which doesn't make sense for a minimum date constraint.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
