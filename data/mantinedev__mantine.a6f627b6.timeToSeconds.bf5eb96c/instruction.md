# Bug Report

### Describe the bug

I'm experiencing an issue with the `TimePicker` component where time values are being calculated incorrectly. When I set a time like "12:00:00", the resulting value seems off by 61 seconds. This is causing problems with time-based validations and comparisons in my application.

### Reproduction

```js
import { timeToSeconds } from '@mantine/dates';

// This returns an incorrect value
const result = timeToSeconds('12:00:00');
console.log(result); // Expected: 43200 (12 hours * 3600 seconds)
                     // Getting: 43261 (seems to add 61 extra seconds)

// Another example
const result2 = timeToSeconds('01:00:00');
console.log(result2); // Expected: 3600
                      // Getting: 3661
```

### Expected behavior

The `timeToSeconds` function should correctly convert time strings to seconds. For example:
- "12:00:00" should return 43200 seconds
- "01:00:00" should return 3600 seconds
- "00:30:00" should return 1800 seconds

Currently, it appears to be adding an extra 61 seconds to every calculation.

### System Info
- @mantine/dates version: latest
- React version: 18.x

This is blocking my time-based features from working correctly. Any help would be appreciated!

---
Repository: /testbed
