# Bug Report

### Describe the bug

The `__onDayClick` handler is not being triggered when clicking on day cells in the calendar component. I'm using the component with the `__onDayClick` prop but the callback function never gets called.

### Reproduction

```jsx
const [selectedDate, setSelectedDate] = useState(null);

<DatePicker
  __onDayClick={(date) => {
    console.log('Day clicked:', date);
    setSelectedDate(date);
  }}
/>
```

When clicking on any day in the calendar, nothing happens. The console.log statement never executes and the state doesn't update.

### Expected behavior

The `__onDayClick` callback should be invoked with the date string when a user clicks on a day cell in the calendar.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
