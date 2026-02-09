# Bug Report

### Describe the bug

When working with date picker components that have multiple tables (like multiple months displayed), the month navigation and day selection seems to be affected. The component appears to only consider days from the first table that has buttons, and it's now filtering out disabled buttons which changes the expected behavior.

### Reproduction

```jsx
import { DatePicker } from '@mantine/dates';

// Component with multiple month tables
<DatePicker 
  type="multiple"
  numberOfColumns={2}
  defaultValue={new Date()}
/>
```

When rendering multiple months side by side, interactions with days in the second month don't work as expected. It seems like the component is only looking at the first table with buttons instead of collecting all day buttons from all visible month tables.

### Expected behavior

All day buttons from all visible month tables should be accessible and interactable, regardless of which table they're in. Disabled buttons should still be included in the selection logic to maintain proper indexing.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
