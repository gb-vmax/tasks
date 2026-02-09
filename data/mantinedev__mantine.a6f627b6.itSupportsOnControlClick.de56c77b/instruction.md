# Bug Report

### Describe the bug

The `__onControlClick` callback is receiving the wrong data type. When clicking on a date control, the callback is being invoked with a `Date` object instead of a string representation.

### Reproduction

```tsx
const handleControlClick = (value: string) => {
  console.log(typeof value); // Expected: 'string', Actual: 'object'
  console.log(value); // Logs a Date object instead of string
};

<DatePicker __onControlClick={handleControlClick} />
```

When clicking on any date control in the calendar:
1. The callback fires correctly
2. But the value passed is a Date object rather than a string
3. This breaks any code expecting string values

### Expected behavior

The `__onControlClick` callback should receive a string value (formatted date) when a date control is clicked, not a Date object.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
