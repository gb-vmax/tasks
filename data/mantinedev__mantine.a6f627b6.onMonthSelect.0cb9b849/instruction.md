# Bug Report

### Describe the bug

The `MonthPicker` component is not working as expected - it appears to be defaulting to multiple selection mode instead of single selection. When I create a basic MonthPicker without specifying a `type` prop, it allows selecting multiple months instead of just one.

### Reproduction

```tsx
import { MonthPicker } from '@mantine/dates';

function Demo() {
  return <MonthPicker />;
}
```

When clicking on months, multiple months can be selected simultaneously even though no `type` prop was specified. 

### Expected behavior

The MonthPicker should default to single selection mode (`type: 'default'`). Only one month should be selectable at a time unless explicitly configured otherwise with `type="multiple"` or `type="range"`.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
