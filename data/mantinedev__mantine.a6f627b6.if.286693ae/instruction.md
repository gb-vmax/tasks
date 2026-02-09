# Bug Report

### Describe the bug

I'm experiencing an issue with the Calendar component where the level clamping logic doesn't work correctly when `minLevel` or `maxLevel` is set to `'month'` (which corresponds to level 0). The calendar fails to properly clamp to the month level, and instead seems to fall back to an incorrect default value.

### Reproduction

```tsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return (
    <Calendar
      minLevel="month"
      maxLevel="month"
      defaultLevel="month"
    />
  );
}
```

When the calendar is configured to only allow the month level view, it doesn't respect this constraint. The level clamping appears to treat the month level (0) as falsy and falls back to an incorrect value instead of recognizing it as a valid level.

### Expected behavior

The calendar should properly clamp to the month level when `minLevel` or `maxLevel` is set to `'month'`. Level 0 (month) should be treated as a valid level value, not as a falsy value that triggers the fallback logic.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
