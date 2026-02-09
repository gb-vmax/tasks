# Bug Report

### Describe the bug

The `YearPicker` component is not behaving as expected when used without explicitly specifying a `type` prop. It seems to be defaulting to `'multiple'` selection mode instead of `'default'` (single selection), which causes unexpected behavior when selecting years.

### Reproduction

```tsx
import { YearPicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState<Date | null>(null);
  
  return (
    <YearPicker 
      value={value} 
      onChange={setValue}
    />
  );
}
```

When clicking on a year, the component allows selecting multiple years instead of just one. The selected year doesn't replace the previous selection like it should in single-select mode.

### Expected behavior

By default, the `YearPicker` should work in single selection mode (`type='default'`), allowing only one year to be selected at a time. When a new year is clicked, it should replace the previously selected year.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
