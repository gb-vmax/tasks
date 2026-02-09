# Bug Report

### Describe the bug

The heatmap weekday names rotation is not working correctly. When setting `firstDayOfWeek` prop, the weekday labels appear in the wrong order or shifted incorrectly.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

// When firstDayOfWeek is set to 0 (Sunday), the weekday names don't match the actual days
<Heatmap
  data={data}
  firstDayOfWeek={0}
/>

// The weekday labels are off by one or more positions
// Expected: Sun, Mon, Tue, Wed, Thu, Fri, Sat
// Actual: Labels are rotated incorrectly
```

### Expected behavior

When `firstDayOfWeek` is set, the weekday names should rotate correctly to start with the specified day. For example:
- `firstDayOfWeek={0}` should show: Sun, Mon, Tue, Wed, Thu, Fri, Sat
- `firstDayOfWeek={1}` should show: Mon, Tue, Wed, Thu, Fri, Sat, Sun

Currently the rotation logic seems to be applying an incorrect offset, causing the weekday labels to not align with the actual data columns.

### System Info
- @mantine/charts version: latest
- Browser: Any

---
Repository: /testbed
