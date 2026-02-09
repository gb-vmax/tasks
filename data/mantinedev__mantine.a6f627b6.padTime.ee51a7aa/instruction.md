# Bug Report

### Describe the bug

The TimePicker component is displaying incorrect time formatting. When entering or displaying time values around 10, they appear with too many leading zeros (e.g., "0010" instead of "10").

### Reproduction

```js
import { TimePicker } from '@mantine/dates';

// When setting time to 10 (hours or minutes)
<TimePicker value={new Date(2024, 0, 1, 10, 10)} />

// The displayed time shows as "0010:0010" instead of "10:10"
```

Try setting the hours or minutes to exactly 10 - the value gets padded with "00" prefix instead of showing just "10".

### Expected behavior

Time values should be padded with a single leading zero only when less than 10:
- `0` → `00`
- `5` → `05`
- `9` → `09`
- `10` → `10` (not `0010`)
- `15` → `15`

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
