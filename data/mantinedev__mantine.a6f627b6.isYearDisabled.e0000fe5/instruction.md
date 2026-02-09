# Bug Report

### Describe the bug

The year picker in the date component is disabling the wrong years. Years that should be selectable are being disabled, and years that should be disabled are being marked as selectable.

### Reproduction

```js
import { YearPicker } from '@mantine/dates';

// Set minDate to 2020 and maxDate to 2025
<YearPicker 
  minDate={new Date(2020, 0, 1)} 
  maxDate={new Date(2025, 11, 31)} 
/>
```

When rendering the year picker with the above configuration:
- Years 2020-2025 are disabled (but they should be enabled)
- Years outside this range (like 2019, 2026) are enabled (but they should be disabled)

The behavior is completely inverted from what's expected.

### Expected behavior

Years within the minDate and maxDate range should be selectable, and years outside this range should be disabled.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
