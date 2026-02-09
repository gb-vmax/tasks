# Bug Report

### Describe the bug

The date picker is not allowing selection of valid dates when `maxDate` is not provided. When no `maxDate` prop is set, all dates are being treated as invalid and cannot be selected.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  return (
    <DatePicker 
      // No maxDate specified
    />
  );
}
```

When rendered, the date picker doesn't allow any date to be selected. All dates appear to be disabled even though there's no maximum date constraint.

### Expected behavior

When `maxDate` is not provided, all dates should be selectable (no upper bound restriction). The date picker should work normally without any date restrictions.

### System Info
- @mantine/dates version: latest
- Browser: Chrome

---
Repository: /testbed
