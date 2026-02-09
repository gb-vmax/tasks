# Bug Report

### Describe the bug

After a recent update, the year picker is displaying incorrectly. The year buttons appear to have extra whitespace or characters prepended to them, and the selector used to find year buttons in the component doesn't seem to be targeting the correct elements anymore.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function Demo() {
  return (
    <YearPicker 
      date={new Date(2024, 0, 1)}
    />
  );
}
```

When inspecting the rendered output, the year buttons have unexpected content at the beginning of their text. The years should display as "2024", "2025", etc., but they seem to have additional characters or formatting issues.

### Expected behavior

Year buttons should display clean year values without any extra characters or whitespace at the start. The component should correctly query and display year names from the table structure.

### System Info
- @mantine/dates version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
