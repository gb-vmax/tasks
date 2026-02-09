# Bug Report

### Describe the bug

When using the `__getDayRef` callback prop in date picker components, the ref keys are being stored with the wrong separator format. I'm trying to access day refs using the `rowIndex.cellIndex` format (e.g., `'0.0'`), but it seems like the internal implementation is using a different format.

### Reproduction

```tsx
const daysRefs = {};

<DatePickerComponent
  __getDayRef={(rowIndex, cellIndex, node) => {
    daysRefs[`${rowIndex}.${cellIndex}`] = node;
  }}
/>

// Later trying to access the first day:
const firstDay = daysRefs['0.0']; // Returns undefined
```

### Expected behavior

The day refs should be accessible using the `'rowIndex.cellIndex'` format as documented. When I try to access `daysRefs['0.0']`, it should return the HTMLButtonElement for the first day of the calendar, but it's coming back as undefined.

Also noticing that the total number of day refs seems off - I'm expecting 35 days (5 weeks × 7 days) but getting a different count.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
