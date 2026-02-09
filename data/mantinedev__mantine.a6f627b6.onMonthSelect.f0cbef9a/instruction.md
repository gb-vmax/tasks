# Bug Report

### Describe the bug

The `MonthPicker` component is now defaulting to `type: 'range'` instead of `type: 'default'`, which breaks existing implementations that rely on the default single-date selection behavior. When using the component without explicitly setting the `type` prop, it unexpectedly behaves as a range picker.

### Reproduction

```tsx
import { MonthPicker } from '@mantine/dates';

function App() {
  const [value, setValue] = useState<Date | null>(null);
  
  return (
    <MonthPicker
      value={value}
      onChange={setValue}
    />
  );
}
```

In this example, the picker now allows selecting a range of months instead of a single month, even though no `type` prop was specified.

### Expected behavior

The `MonthPicker` should default to single month selection (`type: 'default'`) when no `type` prop is provided. Range selection should only be enabled when explicitly setting `type="range"`.

### System Info

- @mantine/dates version: latest
- React version: 18.x

This appears to be a regression as the component previously worked correctly with single month selection by default.

---
Repository: /testbed
