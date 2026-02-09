# Bug Report

### Describe the bug

The `DateInput` component is not accepting `null` as a valid date value and is incorrectly rejecting dates that match the `maxDate` boundary.

### Reproduction

```jsx
import { DateInput } from '@mantine/dates';

// Issue 1: null is treated as invalid
const [value, setValue] = useState(null);
<DateInput value={value} onChange={setValue} />
// Clearing the input or setting value to null causes validation issues

// Issue 2: maxDate boundary is incorrectly exclusive
const maxDate = new Date('2024-12-31');
<DateInput 
  value={new Date('2024-12-31')} 
  maxDate={maxDate}
/>
// Date equal to maxDate is rejected even though it should be valid
```

### Expected behavior

1. `null` should be treated as a valid empty state for DateInput (similar to how form inputs work)
2. When `maxDate` is set, dates equal to `maxDate` should be accepted as valid. The validation should be inclusive of the boundary date, not exclusive.

For example, if `maxDate` is December 31, 2024, selecting December 31, 2024 should be allowed.

### System Info
- @mantine/dates version: latest
- @mantine/core version: latest

---
Repository: /testbed
