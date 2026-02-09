# Bug Report

### Describe the bug

When using the TimePicker component with 12-hour format, the time is being incorrectly converted. It seems like the 12-hour format conversion logic is being applied to the wrong format type, causing times to display incorrectly.

### Reproduction

```js
import { TimePicker } from '@mantine/dates';

// Using 12-hour format
<TimePicker format="12h" value="14:30" />

// Expected: Should show "2:30 PM"
// Actual: Shows the time in 24-hour format instead
```

When I set the format to "12h", the component doesn't properly convert the time to 12-hour format with AM/PM labels. Conversely, when using "24h" format, it appears to be applying the 12-hour conversion when it shouldn't.

### Expected behavior

- When `format="12h"` is specified, times should be displayed in 12-hour format with AM/PM indicators
- When `format="24h"` is specified, times should remain in 24-hour format without conversion

### Additional context

This appears to have started happening recently. The format prop seems to be triggering the opposite behavior - 12h format shows 24h times and vice versa.

---
Repository: /testbed
