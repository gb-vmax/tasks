# Bug Report

### Describe the bug

I'm experiencing an issue with the MonthPicker component where selected months are not being highlighted correctly. When I click on a month to select it, the visual selection appears on the wrong month - specifically, it seems like the selection logic is inverted or off by one.

### Reproduction

```jsx
import { MonthPicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState('2024-03-01');
  
  return (
    <MonthPicker
      value={value}
      onChange={setValue}
      year={2024}
    />
  );
}
```

When I click on March (month index 2), the component highlights a different month instead. The value updates correctly in the state, but the visual feedback in the UI doesn't match the selected month.

### Expected behavior

When a month is selected, that specific month should be visually highlighted in the picker. The selected state should match the actual value being set.

### System Info

- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
