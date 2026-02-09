# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect time format when using 24-hour format. It appears that 12-hour format (AM/PM) is being used even when the format is explicitly set to '24h'.

### Reproduction

```js
import { TimePicker } from '@mantine/dates';

// Setting format to '24h'
<TimePicker format="24h" />

// When selecting a time, it displays in 12-hour format with AM/PM
// instead of 24-hour format
```

### Expected behavior

When `format="24h"` is set, the TimePicker should display time in 24-hour format (e.g., "13:30", "23:45") without AM/PM indicators. Currently it's showing 12-hour format with AM/PM even when 24h format is specified.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
