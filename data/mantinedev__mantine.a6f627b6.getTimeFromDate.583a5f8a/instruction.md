# Bug Report

### Describe the bug

The `TimeValue` component is displaying incorrect time values. When passing a Date object, the hours, minutes, and seconds are not being formatted correctly. The output appears to be missing minutes in some cases and always shows seconds even when they shouldn't be displayed.

### Reproduction

```js
import { TimeValue } from '@mantine/dates';

// Create a date object with specific time
const date = new Date('2024-01-15T14:30:45');

// Display time without seconds
<TimeValue value={date} withSeconds={false} />
// Expected: 14:30
// Actual: Shows incorrect format with missing or wrong values

// Display time with seconds
<TimeValue value={date} withSeconds={true} />
// Expected: 14:30:45
// Actual: Shows incorrect format
```

### Expected behavior

The component should format the time correctly:
- When `withSeconds={false}`, it should display `HH:MM` (e.g., "14:30")
- When `withSeconds={true}`, it should display `HH:MM:SS` (e.g., "14:30:45")
- Hours and minutes should always be present and in the correct positions

### System Info

- @mantine/dates version: latest
- Browser: Chrome/Firefox

This seems to have broken recently, as the time formatting was working correctly before. The hours, minutes, and seconds are appearing in the wrong order or missing entirely.

---
Repository: /testbed
