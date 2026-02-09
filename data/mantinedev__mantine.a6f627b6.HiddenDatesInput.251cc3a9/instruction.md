# Bug Report

### Describe the bug
The `HiddenDatesInput` component is not properly formatting date values before passing them to the hidden input field. The formatted value is being calculated but then discarded, and the raw `value` prop is used instead.

### Reproduction
```jsx
import { HiddenDatesInput } from '@mantine/dates';

// Using HiddenDatesInput with a Date object
<HiddenDatesInput 
  name="dateField"
  value={new Date('2024-01-15')}
  type="default"
/>

// The hidden input receives the raw Date object instead of a formatted string
// Expected: ISO string or formatted date string
// Actual: [object Date] or similar
```

### Expected behavior
The hidden input should contain a properly formatted date string based on the `type` and `withTime` props. The `formatValue` function should be applied to transform the date value before it's set as the input's value attribute.

### System Info
- @mantine/dates version: latest
- Browser: Any

---
Repository: /testbed
