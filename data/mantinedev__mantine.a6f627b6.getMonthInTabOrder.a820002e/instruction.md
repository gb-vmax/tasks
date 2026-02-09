# Bug Report

### Describe the bug

When using the MonthsList component with `getMonthControlProps` to disable specific months, the keyboard navigation is not working correctly. The tab order seems to be selecting disabled months instead of enabled ones, making it impossible to navigate to the available months using the keyboard.

### Reproduction

```tsx
import { MonthsList } from '@mantine/dates';

function Demo() {
  return (
    <MonthsList
      getMonthControlProps={(month) => {
        // Disable some months
        if (month.getMonth() === 0 || month.getMonth() === 1) {
          return { disabled: true };
        }
        return {};
      }}
    />
  );
}
```

Steps to reproduce:
1. Create a MonthsList component with some months disabled via `getMonthControlProps`
2. Try to use keyboard navigation (Tab key) to navigate through the months
3. The focus goes to disabled months instead of enabled ones

### Expected behavior

The tab order should only include enabled months. When navigating with the keyboard, focus should skip over disabled months and only land on months that can be selected.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
