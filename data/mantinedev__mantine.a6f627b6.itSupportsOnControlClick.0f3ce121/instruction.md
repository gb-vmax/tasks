# Bug Report

### Describe the bug

When clicking on date controls in calendar components, the `__onControlClick` callback is being triggered before the actual click event occurs. This causes the callback to fire prematurely without any arguments being passed.

### Reproduction

```jsx
const handleControlClick = (value) => {
  console.log('Clicked date:', value);
};

<DatePicker
  __onControlClick={handleControlClick}
  // ... other props
/>
```

When clicking on a date button in the calendar:
1. The callback fires immediately
2. No date value is passed to the callback
3. The expected date string argument is missing

### Expected behavior

The `__onControlClick` callback should only fire after the user actually clicks a date control, and it should receive the date value as a string argument.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
