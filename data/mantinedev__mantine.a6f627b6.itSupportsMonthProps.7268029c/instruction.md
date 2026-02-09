# Bug Report

### Describe the bug

The calendar is marking incorrect days as weekends and outside days. When rendering a month view, the `data-weekend` and `data-outside` attributes are being applied to the wrong day elements.

### Reproduction

```js
import { Month } from '@mantine/dates';

function Demo() {
  return (
    <Month 
      month={new Date(2024, 0, 1)} // January 2024
    />
  );
}
```

When inspecting the rendered calendar:
- Day 4 (Thursday) is not marked as weekend when it should be
- Day 5 (Friday) is marked as weekend when it shouldn't be  
- Day 7 (Sunday) is not marked as weekend when it should be
- Day 4 at the start of the month is marked as outside when it's actually part of the current month

### Expected behavior

The calendar should correctly identify:
- Weekends (Saturday and Sunday) with the `data-weekend` attribute
- Days outside the current month with the `data-outside` attribute

It seems like there might be an off-by-one error or the week is starting on the wrong day.

### System Info
- @mantine/dates: latest
- @mantine/core: latest

---
Repository: /testbed
