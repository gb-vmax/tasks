# Bug Report

### Describe the bug

The `MonthPicker` component is not working as expected. When I use it without explicitly setting the `type` prop, it's behaving as if `type="range"` is set, but the documentation and TypeScript types suggest it should default to `type="default"`.

### Reproduction

```tsx
import { MonthPicker } from '@mantine/dates';

function MyComponent() {
  const [value, setValue] = useState<Date | null>(null);
  
  return (
    <MonthPicker
      value={value}
      onChange={setValue}
    />
  );
}
```

When clicking on a month, the component behaves like a range picker (expecting two selections) instead of a single month picker. This is confusing because:
1. The TypeScript types indicate `type` defaults to `'default'`
2. The component signature suggests single selection should be the default behavior

### Expected behavior

Without specifying a `type` prop, the `MonthPicker` should work in single-selection mode (default behavior), not range selection mode.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
