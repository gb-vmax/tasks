# Bug Report

### Describe the bug

The `__onDayKeyDown` callback is receiving the wrong parameter. When handling keyboard events on calendar day cells, the callback is being passed the event object instead of the expected payload containing day information (rowIndex, cellIndex, date).

### Reproduction

```jsx
<DatePicker
  month="2022-04-11"
  __onDayKeyDown={(event, payload) => {
    console.log(payload);
    // Expected: { rowIndex: 0, cellIndex: 0, date: '2022-03-28' }
    // Actual: KeyboardEvent object
  }}
/>
```

Steps to reproduce:
1. Set up a date picker component with `__onDayKeyDown` handler
2. Trigger a keyboard event (like space) on a day cell
3. Check what's being passed to the callback

The callback receives the keyboard event as the first parameter instead of the payload with day information. This makes it impossible to access the row/cell indices and date information when handling keyboard interactions.

### Expected behavior

The `__onDayKeyDown` callback should receive the payload object containing `rowIndex`, `cellIndex`, and `date` properties, allowing developers to properly handle keyboard navigation and interactions with specific calendar days.

---
Repository: /testbed
