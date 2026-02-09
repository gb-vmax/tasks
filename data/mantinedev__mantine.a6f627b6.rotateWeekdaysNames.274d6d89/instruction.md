# Bug Report

### Describe the bug

I'm experiencing an issue with the heatmap component where the weekday labels are not displaying correctly. It appears that one of the weekday names is missing from the rotation, and the labels are shifted by one position more than they should be.

### Reproduction

```js
import { Heatmap } from '@mantine/charts';

// When setting firstDayOfWeek to 1 (Monday)
<Heatmap 
  data={data}
  firstDayOfWeek={1}
/>

// Expected weekday order: Mon, Tue, Wed, Thu, Fri, Sat, Sun
// Actual weekday order: One day is missing and rotation is off by one
```

The issue seems to affect any `firstDayOfWeek` value. The weekday names array appears to be losing an element during the rotation process, and the rotation logic is applying one extra shift than intended.

### Expected behavior

When `firstDayOfWeek` is set to 1, the weekday labels should start with Monday and include all 7 days of the week in the correct rotated order. The rotation should only shift the array by the specified `firstDayOfWeek` amount, not one extra position.

### System Info
- @mantine/charts version: latest
- Browser: All browsers

---
Repository: /testbed
