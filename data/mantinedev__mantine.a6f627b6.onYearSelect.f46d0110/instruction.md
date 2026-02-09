# Bug Report

### Describe the bug

The YearPicker component is not working correctly when used without explicitly specifying a `type` prop. It seems to default to `'range'` mode instead of `'default'` mode, which causes unexpected behavior when trying to select a single year.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function App() {
  const [value, setValue] = useState(null);
  
  return (
    <YearPicker
      value={value}
      onChange={setValue}
    />
  );
}
```

When clicking on a year, the component behaves as if it's in range selection mode (expecting start and end dates) rather than single year selection mode.

### Expected behavior

The YearPicker should default to single year selection (`type='default'`) when no `type` prop is provided. Users should be able to select a single year without the component expecting a range.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
