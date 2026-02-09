# Bug Report

### Describe the bug

The `__onDayKeydown` callback is not being triggered when pressing the Space key on a date picker day cell. I expected the callback to fire when I press Space to select a date, but nothing happens.

### Reproduction

```jsx
const handleDayKeydown = (event) => {
  console.log('Day keydown:', event);
};

<DatePicker
  __onDayKeydown={handleDayKeydown}
  defaultDate={new Date(2022, 2, 28)}
/>
```

Steps to reproduce:
1. Render a DatePicker component with the `__onDayKeydown` callback
2. Focus on a day cell in the calendar
3. Press the Space key
4. The callback doesn't fire

### Expected behavior

The `__onDayKeydown` callback should be triggered when pressing the Space key on a focused day cell, similar to how it works with the Enter key. This would allow users to select dates using the Space bar, which is a common keyboard interaction pattern.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
