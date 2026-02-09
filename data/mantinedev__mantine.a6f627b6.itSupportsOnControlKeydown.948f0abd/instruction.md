# Bug Report

### Describe the bug

The `__onControlKeyDown` callback is being triggered with incorrect `rowIndex` values when using keyboard navigation in date picker components. When pressing Enter on a calendar control, the callback receives `rowIndex: 1` instead of the expected `rowIndex: 0`.

### Reproduction

```jsx
const handleKeyDown = (payload) => {
  console.log(payload);
  // Expected: { rowIndex: 0, cellIndex: 0, date: '...' }
  // Actual: { rowIndex: 1, cellIndex: 0, date: '...' }
};

<DatePicker
  __onControlKeyDown={handleKeyDown}
  // ... other props
/>
```

Steps to reproduce:
1. Render a date picker component with `__onControlKeyDown` callback
2. Focus on the first button in the calendar table
3. Press the Enter key
4. Check the `rowIndex` value in the callback payload

### Expected behavior

When pressing Enter on the first row of the calendar, the `__onControlKeyDown` callback should receive `rowIndex: 0` (representing the first row). Currently it's returning `rowIndex: 1` which is off by one.

This affects keyboard navigation logic that relies on accurate row/cell indices for date selection and navigation.

---
Repository: /testbed
