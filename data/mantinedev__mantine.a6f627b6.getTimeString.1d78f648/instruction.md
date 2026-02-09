# Bug Report

### Describe the bug

The TimePicker component is displaying times in the wrong format. When I set the format to 12-hour (`'12h'`), it shows times in 24-hour format instead, and vice versa. The AM/PM indicator is also not appearing when it should be.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

// Using 12-hour format
<TimePicker format="12h" value={new Date(2024, 0, 1, 14, 30)} />
// Expected: "2:30 PM"
// Actual: "14:30"

// Using 24-hour format
<TimePicker format="24h" value={new Date(2024, 0, 1, 14, 30)} />
// Expected: "14:30"
// Actual: "2:30 PM"
```

### Expected behavior

- When `format="12h"` is set, the time should display in 12-hour format with AM/PM
- When `format="24h"` is set, the time should display in 24-hour format without AM/PM
- The displayed format should match the specified format prop

### System Info

- @mantine/dates version: latest
- React version: 18.x

This seems to have started recently, possibly after a recent update. The formats appear to be inverted from what they should be.

---
Repository: /testbed
