# Bug Report

### Describe the bug

The `firstDayOfWeek` prop seems to have an off-by-one error when set to `0`. When I set `firstDayOfWeek={0}`, the week starts with Monday instead of Sunday. Based on standard conventions where 0 = Sunday, 1 = Monday, etc., this doesn't seem right.

### Reproduction

```jsx
import { Calendar } from '@mantine/dates';

function Demo() {
  return (
    <Calendar firstDayOfWeek={0} />
  );
}
```

When rendered, the weekday headers show: `Mo, Tu, We, Th, Fr, Sa, Su`

### Expected behavior

When `firstDayOfWeek={0}`, the week should start with Sunday, showing weekday headers as: `Su, Mo, Tu, We, Th, Fr, Sa`

Similarly, there might be an issue with the `weekdayFormat` prop. When using a custom formatter that extracts a character from the formatted day name, it seems to be getting the wrong character index.

### System Info

- @mantine/dates: latest
- @mantine/core: latest
- React: 18.x

---
Repository: /testbed
