# Bug Report

### Describe the bug

The clear button in TimePicker is not showing up when it should. I have `clearable` prop set to `true` but the clear button only appears when ALL time fields (hours, minutes, seconds, and amPm) have values. 

### Reproduction

```jsx
import { TimePicker } from '@mantine/dates';

function Demo() {
  const [value, setValue] = useState(new Date());
  
  return (
    <TimePicker
      clearable
      value={value}
      onChange={setValue}
      withSeconds
    />
  );
}
```

Steps to reproduce:
1. Set up a TimePicker with `clearable` prop
2. Enter a value for hours only (or any single field)
3. The clear button doesn't appear

### Expected behavior

The clear button should appear as soon as ANY of the time fields have a value, not only when all fields are filled. If I enter just the hours, I should be able to clear it.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
