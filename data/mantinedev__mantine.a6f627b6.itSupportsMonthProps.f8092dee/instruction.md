# Bug Report

### Describe the bug

I'm experiencing an issue with the calendar component where the weekend detection seems to be incorrect. When rendering a month view, some days that should be marked as weekends are not being marked correctly, and the total number of days displayed is inconsistent with different `firstDayOfWeek` settings.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

// Render calendar with default settings for April 2022
<Calendar month={new Date(2022, 3, 1)} />

// Check the days - the 5th day in the grid (index 4) should be a weekend day
// but it's not being marked with the data-weekend attribute

// Also, when setting firstDayOfWeek to Saturday:
<Calendar month={new Date(2022, 3, 1)} firstDayOfWeek={6} />

// The number of days rendered seems wrong - getting 35 days instead of expected 42
```

### Expected behavior

1. Days that fall on weekends should have the `data-weekend` attribute set correctly
2. When `firstDayOfWeek` is set to Saturday (6), the calendar should render 42 days (6 weeks) to properly display the month with outside dates
3. Weekend detection should work consistently regardless of the `firstDayOfWeek` setting

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
