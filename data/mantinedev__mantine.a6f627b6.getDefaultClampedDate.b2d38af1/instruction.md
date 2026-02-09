# Bug Report

### Describe the bug

When using date picker components with `maxDate` constraint, the default date is not being clamped correctly. If today's date is after the `maxDate`, the component should default to `maxDate`, but instead it's defaulting to today's date which is outside the allowed range.

### Reproduction

```js
import { DatePicker } from '@mantine/dates';
import dayjs from 'dayjs';

// Set maxDate to yesterday
const maxDate = dayjs().subtract(1, 'day').toDate();

// DatePicker defaults to today instead of maxDate
<DatePicker maxDate={maxDate} />
```

### Expected behavior

When today's date exceeds the `maxDate` constraint, the date picker should automatically clamp to and display the `maxDate` as the default value, not today's date.

### System Info

- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
