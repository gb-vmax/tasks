# Bug Report

### Describe the bug

When using the `__getDayRef` callback with calendar components, the refs object is missing one day reference. It appears that the first day (key `'0.0'`) is not being included in the refs collection, and instead the refs start from `'1.0'`.

### Reproduction

```tsx
const daysRefs = {};

<CalendarComponent
  __getDayRef={(rowIndex, cellIndex, node) => {
    daysRefs[`${rowIndex}.${cellIndex}`] = node;
  }}
/>

// Expected: daysRefs should have 35 entries starting from '0.0'
// Actual: daysRefs only has 34 entries and starts from '1.0'
console.log(Object.keys(daysRefs).length); // Returns 34 instead of 35
console.log(daysRefs['0.0']); // undefined
console.log(daysRefs['1.0']); // HTMLButtonElement
```

### Expected behavior

The `__getDayRef` callback should be called for all day cells in the calendar, including the first day at index `'0.0'`. The refs object should contain 35 entries (7 columns × 5 rows) with keys starting from `'0.0'`.

### System Info

- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
