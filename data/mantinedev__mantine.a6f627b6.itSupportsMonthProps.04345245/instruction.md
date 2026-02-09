# Bug Report

### Describe the bug

I'm experiencing an issue with the month calendar component where the number of rendered day cells is incorrect. The calendar is rendering one less day cell than expected, which causes the layout to break and some dates to be missing from the display.

### Reproduction

When rendering a month calendar with default settings (April 2022), the component should display all days including outside dates from adjacent months. However, it appears that one day cell is missing from the rendered output.

```jsx
// Default month rendering
<MonthCalendar month={new Date(2022, 3, 1)} />
// Expected: 35 day cells (5 weeks)
// Actual: Only 34 cells are rendered
```

Similarly, when setting `firstDayOfWeek={6}` (Saturday), the calendar should span 6 weeks (42 days) but only renders 41 cells.

### Additional observations

- The `data-outside` attribute is being applied to the wrong day cells - it looks like there's an off-by-one error where the attribute checks are targeting incorrect indices
- The `data-weekend` attribute also appears to be checking the wrong day indices, causing weekends to be marked incorrectly

This is causing visual issues where the calendar grid doesn't align properly and some dates are either missing or marked with incorrect attributes.

### Expected behavior

The calendar should render the correct number of day cells:
- 35 cells for a 5-week month (default)
- 42 cells for a 6-week month (when firstDayOfWeek is set)
- Attributes like `data-outside` and `data-weekend` should be applied to the correct day cells based on their actual index position

### System Info
- Package: @mantine/dates
- Component: Month calendar components

---
Repository: /testbed
