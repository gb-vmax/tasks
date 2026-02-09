# Bug Report

### Describe the bug

The clear button in the TimePicker component is showing up at the wrong times. It appears when all time fields are empty (when it shouldn't be visible), and doesn't appear when there are actual values to clear.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(null);
  
  return (
    <TimePicker 
      value={value} 
      onChange={setValue}
      clearable
    />
  );
}
```

Steps to reproduce:
1. Render a TimePicker with `clearable` prop enabled
2. Leave all fields empty - the clear button shows up (shouldn't be visible)
3. Enter some time values - the clear button disappears (should be visible)

### Expected behavior

The clear button should only appear when there are actual values in the time fields (hours, minutes, seconds, or AM/PM). When all fields are empty, the clear button should be hidden.

Currently it's doing the opposite - showing when empty and hiding when there are values.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
