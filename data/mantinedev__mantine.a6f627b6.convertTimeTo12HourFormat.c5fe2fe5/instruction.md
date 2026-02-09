# Bug Report

### Describe the bug
The TimePicker component is not correctly converting 12-hour time format. When displaying times in 12-hour format, 12:00 PM is showing as 12:00 AM, and the AM/PM indicator appears to be incorrect for noon hour.

### Reproduction
```js
import { TimePicker } from '@mantine/dates';

// When setting time to 12:00 (noon)
const time = new Date();
time.setHours(12, 0, 0);

// The TimePicker displays 12:00 AM instead of 12:00 PM
<TimePicker value={time} />
```

### Expected behavior
- 12:00 (noon) should display as 12:00 PM
- 00:00 (midnight) should display as 12:00 AM
- The AM/PM indicator should correctly reflect whether the time is before or after noon

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
