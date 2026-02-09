# Bug Report

### Describe the bug

When using `TimeValue` component with `withSeconds={false}`, the formatted time output is incorrect. The minutes are being replaced with the hours value, resulting in duplicate hour values in the output string.

### Reproduction

```js
import { getFormattedTime } from '@mantine/dates';

const date = new Date('2024-01-01T14:30:45');

// Without seconds
const result = getFormattedTime({ date, withSeconds: false });
console.log(result); // Expected: "14:30", Actual: "14:14"

// With seconds also affected
const resultWithSeconds = getFormattedTime({ date, withSeconds: true });
console.log(resultWithSeconds); // Expected: "14:30:45", Actual: "14:30:30"
```

### Expected behavior

The time should be formatted correctly:
- Without seconds: `"14:30"`
- With seconds: `"14:30:45"`

Instead, the minutes position is showing the wrong value (hours or minutes depending on the `withSeconds` flag).

### System Info

- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
