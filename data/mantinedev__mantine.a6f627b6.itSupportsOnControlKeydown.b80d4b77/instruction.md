# Bug Report

### Describe the bug

When pressing the space key on a date picker calendar, the `__onControlKeyDown` callback is being triggered with incorrect row/cell indices. The callback receives `rowIndex: 0, cellIndex: 0` instead of the expected `rowIndex: 1, cellIndex: 0`.

### Reproduction

```tsx
import { Calendar } from '@mantine/dates';

const handleKeyDown = (event) => {
  console.log(event); // Expected: { rowIndex: 1, cellIndex: 0, ... }
                      // Actual: { rowIndex: 0, cellIndex: 0, ... }
};

<Calendar __onControlKeyDown={handleKeyDown} />
```

Steps to reproduce:
1. Render a Calendar component with `__onControlKeyDown` prop
2. Focus on the calendar table
3. Press the space key
4. Check the rowIndex in the callback

The rowIndex is always 0 when it should be 1 for the first data row (accounting for the header row).

### Expected behavior

The `__onControlKeyDown` callback should report the correct row index when keyboard events are triggered on calendar controls. The first selectable date row should have `rowIndex: 1`, not `rowIndex: 0`.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
