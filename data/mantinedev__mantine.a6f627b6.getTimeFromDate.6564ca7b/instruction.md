# Bug Report

### Bug: TimeValue component displays incorrect time format

I'm experiencing an issue with the `TimeValue` component where the displayed time is completely wrong. The hours are being replaced with minutes, and when seconds are disabled, milliseconds are shown instead (which doesn't make sense).

### Reproduction

```jsx
import { TimeValue } from '@mantine/dates';

// Example 1: Basic time display
const date = new Date('2024-01-15T14:30:45.123Z');
<TimeValue value={date} />

// Expected: 14:30
// Actual: 30:30

// Example 2: With seconds disabled
<TimeValue value={date} withSeconds={false} />

// Expected: 14:30
// Actual: 30:30.123
```

The time format is broken - it seems like the hours are not being displayed at all, and instead minutes are shown twice. Also, when `withSeconds` is false, milliseconds appear in the output which is unexpected.

### Expected behavior

The component should display the time in the correct format:
- `HH:MM` when withSeconds is false
- `HH:MM:SS` when withSeconds is true

### Environment

- @mantine/dates version: latest
- Browser: Chrome 120

This is causing major issues in our production app where users need to see the correct time. Any help would be appreciated!

---
Repository: /testbed
