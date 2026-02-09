# Bug Report

### Describe the bug

When using the Calendar component with `level={0}` (which should represent 'month' level), the level is not being applied correctly. The calendar seems to ignore the level prop when it's explicitly set to `0` and falls back to a default value instead.

### Reproduction

```tsx
import { Calendar } from '@mantine/dates';

// This doesn't work as expected
<Calendar level={0} />

// The calendar ignores level={0} and uses fallback behavior
// Expected: Should display month level view
// Actual: Falls back to default level
```

### Expected behavior

When `level={0}` is passed to the Calendar component, it should be treated as a valid level value (equivalent to 'month') and display the month view. The value `0` is a falsy value but should still be recognized as a valid numeric level.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
