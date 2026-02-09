# Bug Report

### Describe the bug

The `onPrevious` callback is not being triggered when clicking the previous button in date picker components. Similarly, the `onLevelClick` callback is not firing when the level control is clicked.

### Reproduction

```jsx
const [date, setDate] = useState(new Date());
const onPreviousSpy = jest.fn();
const onLevelClickSpy = jest.fn();

<DatePicker
  date={date}
  onPreviousMonth={onPreviousSpy}
  onLevelClick={onLevelClickSpy}
/>
```

Steps to reproduce:
1. Set up a date picker component with `onPreviousMonth` and `onLevelClick` handlers
2. Click the previous month button
3. Click the level control button
4. Check if the callbacks were invoked

### Expected behavior

- Clicking the previous button should trigger the `onPrevious` callback exactly once
- Clicking the level control should trigger the `onLevelClick` callback exactly once

### Current behavior

The callbacks are not being called when their respective controls are clicked. The UI updates correctly but the event handlers are not firing.

---
Repository: /testbed
