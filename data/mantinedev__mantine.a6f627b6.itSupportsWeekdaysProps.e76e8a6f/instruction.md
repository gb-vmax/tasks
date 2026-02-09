# Bug Report

### Describe the bug

The `firstDayOfWeek` prop doesn't seem to be working correctly when changing it dynamically. When I update the `firstDayOfWeek` value, the weekday order in the calendar doesn't update to reflect the new starting day.

### Reproduction

```jsx
const [firstDay, setFirstDay] = useState(0);

// Initially renders with Sunday as first day
<DatePicker firstDayOfWeek={firstDay} />

// Update to start week on Saturday (6)
setFirstDay(6);

// Expected: Week should now start with Saturday
// Actual: Week order remains unchanged, still starts with Sunday
```

### Expected behavior

When `firstDayOfWeek` is changed from `0` (Sunday) to `6` (Saturday), the weekday headers should reorder to show Saturday as the first column, followed by Sunday, Monday, etc.

### Additional context

This appears to be a regression - the prop was working correctly in previous versions. The weekday order should dynamically update when the `firstDayOfWeek` prop changes.

---
Repository: /testbed
