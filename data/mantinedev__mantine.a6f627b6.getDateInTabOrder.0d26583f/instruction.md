# Bug Report

### Describe the bug

I'm experiencing an issue with the date picker where dates that should be excluded are actually being made selectable, and dates that should be selectable are being excluded. The behavior is completely inverted from what I expect.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function Demo() {
  const excludeWeekends = (date) => {
    const day = date.getDay();
    return day === 0 || day === 6; // Should exclude Saturdays and Sundays
  };

  return (
    <DatePicker
      excludeDate={excludeWeekends}
    />
  );
}
```

### Expected behavior

When I provide an `excludeDate` function that returns `true` for weekends, those dates should be disabled/excluded from selection. Instead, **only** weekends are selectable and all weekdays are excluded, which is the opposite of what should happen.

### Additional context

This seems to have broken recently. The date picker is now allowing me to select exactly the dates I'm trying to exclude, while blocking all the dates that should be available.

---
Repository: /testbed
