# Bug Report

### Describe the bug

The `YearPicker` component is not working as expected when used without explicitly setting the `type` prop. It seems to be defaulting to `'multiple'` selection mode instead of `'default'` (single selection), which breaks existing code that relies on the default behavior.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function MyComponent() {
  const [value, setValue] = useState<Date | null>(null);
  
  return (
    <YearPicker 
      value={value}
      onChange={setValue}
    />
  );
}
```

When clicking on a year, the component behaves as if `type="multiple"` was set, allowing multiple year selections instead of just selecting a single year. This is unexpected since the documentation states that `'default'` should be the default type.

### Expected behavior

When no `type` prop is provided, the `YearPicker` should default to single selection mode (`type="default"`), not multiple selection mode.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
