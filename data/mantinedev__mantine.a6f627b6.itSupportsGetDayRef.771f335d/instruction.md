# Bug Report

### Describe the bug

The `__getDayRef` callback is receiving incorrect parameter order for `rowIndex` and `cellIndex`. When the callback is invoked, the indices appear to be swapped, causing refs to be stored with incorrect keys.

### Reproduction

```tsx
const daysRefs = {};

<Calendar
  __getDayRef={(rowIndex, cellIndex, node) => {
    // Expected: rowIndex first, cellIndex second
    // Actual: parameters seem to be in wrong order
    daysRefs[`${rowIndex}.${cellIndex}`] = node;
  }}
/>

// The refs are being stored with swapped indices
// e.g., expecting '0.0' but getting '0.0' with wrong meaning
```

### Expected behavior

When `__getDayRef` is called with `(rowIndex, cellIndex, node)`, the first parameter should represent the row index and the second parameter should represent the cell index. The callback should receive these parameters in the documented order so that refs can be stored correctly.

### System Info

- @mantine/dates latest version

---
Repository: /testbed
