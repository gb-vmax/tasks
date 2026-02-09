# Bug Report

### Describe the bug

When using the date picker component without a `minDate` prop, all dates are being disabled/blocked. The component should allow selecting any date when `minDate` is not specified, but instead it's preventing all date selections.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

function MyComponent() {
  return (
    <DatePicker
      // No minDate specified - all dates should be selectable
      value={new Date()}
      onChange={(date) => console.log(date)}
    />
  );
}
```

### Expected behavior

When `minDate` is not provided (undefined), all dates should be selectable. The date picker should only restrict dates when `minDate` is explicitly set.

### Current behavior

All dates appear to be disabled/unselectable when `minDate` is undefined. The component is unusable without explicitly setting a `minDate` value.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
