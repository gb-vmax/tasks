# Bug Report

### Describe the bug

When using the `__onControlKeyDown` callback with date picker components, the callback is being triggered with incorrect `rowIndex` values. The row index appears to be off by one from what's expected.

### Reproduction

```jsx
const handleKeyDown = (payload) => {
  console.log('Row index:', payload.rowIndex);
  // Expected: rowIndex: 0 for first row
  // Actual: rowIndex: 1
};

<DatePicker
  __onControlKeyDown={handleKeyDown}
/>
```

Steps to reproduce:
1. Set up a date picker component with `__onControlKeyDown` callback
2. Navigate to the first row of the calendar
3. Press space key on a date button
4. Check the rowIndex in the callback payload

### Expected behavior

The `rowIndex` should be `0` when interacting with controls in the first row of the calendar. Currently it's returning `1` instead.

### System Info

- Mantine version: latest
- React version: 18.x

---
Repository: /testbed
