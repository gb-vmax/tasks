# Bug Report

### Describe the bug

The calendar month view is rendering an incorrect number of day cells. When displaying April 2022, the calendar shows 36 cells instead of the expected 35, which causes the layout to break and display an extra row.

### Reproduction

```jsx
<Calendar month={new Date(2022, 3, 1)} />
```

When rendering a month view, the component generates one too many day cells. For April 2022 starting on a Friday, the expected behavior is to show:
- 4 days from the previous month (March 28-31)
- 30 days of April
- 1 day from the next month (May 1)
- Total: 35 cells (5 rows × 7 days)

However, the component is currently rendering 36 cells, which adds an unnecessary 6th row to the calendar.

### Expected behavior

The month view should render exactly 35 day cells (5 complete weeks) for a standard month layout. The last cell should contain May 1st as an outside date, and the calendar should not extend to a 6th row.

### Additional context

This also affects the `data-outside` attribute positioning - the outside dates from the previous month are shifted by one position, causing incorrect styling for days that belong to the current month vs. adjacent months.

---
Repository: /testbed
