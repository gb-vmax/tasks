# Bug Report

### Describe the bug

I'm experiencing an issue with the Heatmap component where passing a date object to functions that calculate date ranges causes unexpected side effects. The original date object gets mutated instead of returning a new date, which breaks my application logic when I need to reuse the same date reference.

### Reproduction

```js
const startDate = new Date('2024-01-01');
const originalTime = startDate.getTime();

// Use the date in heatmap calculations
const nextDate = addDaysToDate(startDate, 7);

// The original date has been modified!
console.log(startDate.getTime() === originalTime); // false - should be true
console.log(startDate); // Now shows 2024-01-08 instead of 2024-01-01
```

This is causing issues in my component where I store a reference date and expect it to remain unchanged when calculating ranges for the heatmap.

### Expected behavior

Date utility functions should return new Date objects without modifying the input date. This is standard practice to avoid unintended side effects.

### System Info
- @mantine/charts version: latest
- React version: 18.x

---
Repository: /testbed
