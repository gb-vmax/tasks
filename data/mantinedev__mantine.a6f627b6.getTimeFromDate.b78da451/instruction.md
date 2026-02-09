# Bug Report

### Describe the bug

I'm experiencing an issue with the TimeValue component where the displayed time format is incorrect. When passing a Date object, the hours are not being displayed correctly - instead, it seems like the minutes are being shown in place of the hours.

### Reproduction

```js
import { getFormattedTime } from '@mantine/dates';

const date = new Date();
date.setHours(14);
date.setMinutes(30);
date.setSeconds(45);

const formatted = getFormattedTime({ value: date, withSeconds: false });
console.log(formatted); // Expected: "14:30" but getting something like "30:30"
```

### Expected behavior

The formatted time should display the correct hours and minutes from the Date object. For example, if the time is 14:30, it should show "14:30", not "30:30".

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
