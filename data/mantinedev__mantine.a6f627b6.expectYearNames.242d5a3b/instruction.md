# Bug Report

### Describe the bug

When rendering a years list in the date picker component, disabled year buttons are being included in the selection, causing incorrect behavior when navigating or selecting years. The component appears to be counting disabled buttons as valid selectable options.

### Reproduction

```jsx
import { YearPicker } from '@mantine/dates';

function Demo() {
  return (
    <YearPicker
      minDate={new Date(2020, 0, 1)}
      maxDate={new Date(2025, 11, 31)}
      defaultValue={new Date(2022, 0, 1)}
    />
  );
}
```

When the years list is rendered with date constraints (minDate/maxDate), the disabled year buttons outside the valid range are being treated as part of the selectable years list. This causes issues when:
1. Trying to programmatically access the list of available years
2. Navigating through years with keyboard controls
3. Validating year selections

### Expected behavior

Disabled year buttons should be excluded from the years list operations. Only enabled/selectable years should be considered when building the list of available options.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
