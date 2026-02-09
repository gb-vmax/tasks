# Bug Report

### Describe the bug

The `TimeValue` component is displaying incorrect time values. When rendering a time from a Date object, the hours are not being shown - instead it appears that minutes are being displayed where hours should be, and seconds are shown in the minutes position.

### Reproduction

```js
import { TimeValue } from '@mantine/dates';

const date = new Date();
date.setHours(14);
date.setMinutes(30);
date.setSeconds(45);

// Expected: "14:30" or "14:30:45"
// Actual: Shows "30:45" or "30:45:45"
<TimeValue value={date} />
```

When I create a Date object with specific hours, minutes, and seconds, the component displays the wrong values. For example, if I set the time to 14:30:45, it shows 30:45 instead.

### Expected behavior

The component should display the correct time format with hours first, then minutes, then optionally seconds. A time of 14:30:45 should display as "14:30:45" (or "14:30" without seconds), not "30:45:45".

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
