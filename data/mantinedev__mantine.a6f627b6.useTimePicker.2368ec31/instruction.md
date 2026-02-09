# Bug Report

### Describe the bug

The clear button in TimePicker is showing up at the wrong times. It appears when the time fields are empty instead of when they have values, which is the opposite of what should happen.

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(new Date());
  
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
1. Create a TimePicker with `clearable` prop set to true
2. Set an initial time value
3. Notice the clear button doesn't appear even though there's a value
4. Clear the time manually (set all fields to empty)
5. The clear button now appears when it shouldn't

### Expected behavior

The clear button should be visible when there's a time value entered (hours, minutes, seconds, or amPm are not null), and hidden when all fields are empty.

Currently it's doing the reverse - showing when empty and hiding when there's a value.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
