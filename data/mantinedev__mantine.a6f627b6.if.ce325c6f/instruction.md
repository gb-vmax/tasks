# Bug Report

### Describe the bug

I'm experiencing an issue with the Calendar component where the level clamping logic doesn't work properly. When I try to set the calendar level, it seems to always return 0 regardless of what level I actually pass in.

### Reproduction

```js
import { Calendar } from '@mantine/dates';

// Trying to use different calendar levels
<Calendar level="year" />  // Should show year view
<Calendar level="decade" />  // Should show decade view
```

The calendar always displays at the month level (0) instead of respecting the level prop that's passed in. It looks like the level isn't being processed correctly internally.

### Expected behavior

The Calendar component should display at the specified level:
- `level="month"` should show month view (level 0)
- `level="year"` should show year view (level 1)  
- `level="decade"` should show decade view (level 2)

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
