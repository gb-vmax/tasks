# Bug Report

### Describe the bug

The TimePicker component is not correctly parsing time strings anymore. When I try to set or read time values, I'm getting incorrect results. It seems like the time string parsing is completely broken.

### Reproduction

```js
import { timeToSeconds } from '@mantine/dates';

// Try to convert a time string to seconds
const result = timeToSeconds('10:30:45');
console.log(result); // Expected: 37845 seconds (10 hours * 3600 + 30 minutes * 60 + 45 seconds)
// But getting a completely wrong value instead
```

### Expected behavior

The `timeToSeconds` function should properly parse time strings in the format `HH:MM:SS` and convert them to the total number of seconds. For example:
- `"01:00:00"` should return `3600` (1 hour)
- `"00:30:00"` should return `1800` (30 minutes)
- `"10:30:45"` should return `37845` (10 hours, 30 minutes, 45 seconds)

Currently, the function is not working at all and returns unexpected values.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
