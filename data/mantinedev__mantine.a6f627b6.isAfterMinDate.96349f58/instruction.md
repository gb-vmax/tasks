# Bug Report

### Describe the bug

When using the date picker with a `minDate` set, dates that should be selectable are being incorrectly disabled. Specifically, dates on or after the minimum date are not being recognized as valid selections.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

// Set minDate to January 1, 2024
<DatePicker minDate={new Date(2024, 0, 1)} />
```

When trying to select dates that are on or after January 1, 2024, they appear as disabled or are not selectable, even though they should be valid according to the `minDate` constraint.

### Expected behavior

All dates on or after the `minDate` should be selectable. The date picker should only disable dates that are strictly before the minimum date.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
