# Bug Report

### Describe the bug

The weekday rotation in the Heatmap component is not working correctly. When setting `firstDayOfWeek`, the weekday labels are being rotated by an incorrect amount, causing them to be misaligned with the actual data.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

// Example with firstDayOfWeek set to 0 (Sunday)
<Heatmap
  data={data}
  firstDayOfWeek={0}
  // Weekdays appear incorrectly rotated
/>

// Example with firstDayOfWeek set to 1 (Monday)
<Heatmap
  data={data}
  firstDayOfWeek={1}
  // Weekdays are double-rotated or off by one
/>
```

### Expected behavior

When `firstDayOfWeek` is set to 0, the weekdays should start with Sunday. When set to 1, they should start with Monday, etc. The rotation should correctly align the weekday names with their corresponding data columns.

Currently, it seems like the weekdays are being rotated one extra time, causing the labels to be off by one position.

### System Info

- @mantine/charts version: latest
- Browser: Any

---
Repository: /testbed
