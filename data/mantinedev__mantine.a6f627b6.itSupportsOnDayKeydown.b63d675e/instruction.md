# Bug Report

### Describe the bug

The `__onDayKeyDown` callback is not being triggered when pressing keys on the calendar table. It seems like keyboard events on the table element itself aren't being properly propagated or handled.

### Reproduction

```jsx
const spy = jest.fn();

<DatePicker
  month="2022-04-11"
  __onDayKeyDown={(event, payload) => {
    spy(payload);
  }}
/>

// Press space key on the table
// Expected: spy to be called with { rowIndex: 0, cellIndex: 0, date: '2022-03-28' }
// Actual: spy is never called
```

### Expected behavior

When keyboard events occur on the calendar table, the `__onDayKeyDown` callback should be invoked with the appropriate payload containing `rowIndex`, `cellIndex`, and `date` information.

### Additional context

This might be related to how keyboard event listeners are attached to the calendar component. The callback works fine when interacting directly with day buttons, but not when events are triggered on the table container itself.

---
Repository: /testbed
