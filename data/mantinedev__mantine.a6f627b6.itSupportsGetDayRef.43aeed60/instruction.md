# Bug Report

### Describe the bug

The `__getDayRef` callback is not storing day references correctly. When using the callback to store references to day elements, the keys are being generated without the separator dot, causing some references to overwrite each other.

### Reproduction

```jsx
const daysRefs = {};

<Calendar
  __getDayRef={(rowIndex, cellIndex, node) => {
    daysRefs[`${rowIndex}${cellIndex}`] = node;
  }}
/>

// Expected: 35 unique keys (5 rows × 7 columns)
// Actual: Only 34 keys are stored
console.log(Object.keys(daysRefs).length); // 34 instead of 35
```

For example, row 1 cell 0 (`1` + `0` = `"10"`) collides with row 0 cell 10 (if it existed), but more importantly, this causes issues with the expected number of stored references.

### Expected behavior

All day references should be stored with unique keys. The callback should generate keys like `"0.0"`, `"0.1"`, etc. to ensure uniqueness, and all 35 day elements (5 weeks × 7 days) should be properly stored.

### System Info
- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
