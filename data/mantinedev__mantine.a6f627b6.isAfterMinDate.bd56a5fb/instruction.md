# Bug Report

### Describe the bug

The date validation logic for minimum dates seems to be inverted. When setting a `minDate` on a date picker component, dates that should be selectable are being disabled, and dates that should be disabled are selectable.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';

// Set minDate to January 15, 2024
const minDate = new Date(2024, 0, 15);

<DatePicker minDate={minDate} />
```

When the date picker is rendered:
- Dates on or after January 15, 2024 are disabled (but should be enabled)
- Dates before January 15, 2024 are enabled (but should be disabled)

### Expected behavior

Dates that are on or after the `minDate` should be selectable/enabled, while dates before the `minDate` should be disabled.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
