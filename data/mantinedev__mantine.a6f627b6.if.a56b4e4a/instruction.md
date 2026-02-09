# Bug Report

### Describe the bug

I'm encountering an issue with the Calendar component where the `clampLevel` function doesn't handle fallback values correctly. When I pass a fallback value, it always returns `0` instead of the actual fallback I provided.

### Reproduction

```js
import { Calendar } from '@mantine/dates';

// When minLevel or maxLevel is undefined with a fallback
<Calendar
  minLevel={undefined}
  maxLevel={undefined}
  defaultLevel="decade"
/>
```

The calendar doesn't respect the level constraints properly when the min/max levels are not set. It seems like the fallback logic is broken and always defaults to `0` regardless of what fallback value is passed internally.

### Expected behavior

When `minLevel` or `maxLevel` are undefined, the calendar should use the provided fallback value (if any) to determine the level constraints. Currently it seems to ignore non-zero fallback values.

### System Info
- @mantine/dates version: latest
- Browser: Chrome 120

---
Repository: /testbed
