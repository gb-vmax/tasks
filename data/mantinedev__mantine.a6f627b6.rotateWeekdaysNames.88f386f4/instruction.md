# Bug Report

### Describe the bug

The `rotateWeekdaysNames` function in the Heatmap component is not correctly rotating weekday names based on the `firstDayOfWeek` parameter. The rotation appears to be happening in the wrong direction.

### Reproduction

```js
import { rotateWeekdaysNames } from '@mantine/charts';

const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

// When firstDayOfWeek is 1 (Monday), expecting Monday to be first
const result = rotateWeekdaysNames(weekdays, 1);
console.log(result);
// Current output: ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
// Expected output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

// When firstDayOfWeek is 3 (Wednesday), expecting Wednesday to be first
const result2 = rotateWeekdaysNames(weekdays, 3);
console.log(result2);
// Current output: ['Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed']
// Expected output: ['Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue']
```

### Expected behavior

When setting `firstDayOfWeek` to a specific day index, that day should appear as the first element in the returned array. For example, if `firstDayOfWeek` is 1 (Monday), the array should start with Monday.

### System Info

- @mantine/charts version: latest
- Browser: All browsers affected

---
Repository: /testbed
