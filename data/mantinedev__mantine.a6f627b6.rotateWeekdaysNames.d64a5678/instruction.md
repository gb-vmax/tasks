# Bug Report

### Describe the bug

The `Heatmap` component is displaying weekday names incorrectly when using a custom `firstDayOfWeek` prop. The weekday labels appear to be rotated by one extra position, causing misalignment between the actual data and the day labels shown.

### Reproduction

```jsx
import { Heatmap } from '@mantine/charts';

// Example: Setting Monday as first day of week
<Heatmap
  data={myData}
  firstDayOfWeek={1}
  weekdayNames={['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']}
/>
```

When `firstDayOfWeek` is set to `1` (Monday), the weekday names are shifted incorrectly. Instead of showing:
```
Mon, Tue, Wed, Thu, Fri, Sat, Sun
```

It shows something like:
```
Tue, Wed, Thu, Fri, Sat, Sun
```

The last weekday name is missing and the rotation seems off by one position.

### Expected behavior

The weekday names should rotate correctly based on the `firstDayOfWeek` value without losing any days. When `firstDayOfWeek={1}`, Monday should appear first, followed by the rest of the days in order, ending with Sunday.

### System Info
- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
