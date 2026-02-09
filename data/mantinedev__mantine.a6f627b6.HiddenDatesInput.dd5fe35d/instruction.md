# Bug Report

### Describe the bug

The `HiddenDatesInput` component is not correctly handling the `withTime` prop. When I explicitly pass `withTime={true}`, the formatted date value doesn't include the time portion, and when I pass `withTime={false}` (or omit it), the time is unexpectedly included.

### Reproduction

```jsx
import { HiddenDatesInput } from '@mantine/dates';

// Example 1: Explicitly setting withTime to true
<HiddenDatesInput 
  value={new Date('2024-01-15T14:30:00')} 
  type="default"
  name="dateWithTime"
  withTime={true}
/>
// Expected: Date formatted with time
// Actual: Date formatted WITHOUT time

// Example 2: Setting withTime to false
<HiddenDatesInput 
  value={new Date('2024-01-15T14:30:00')} 
  type="default"
  name="dateWithoutTime"
  withTime={false}
/>
// Expected: Date formatted without time
// Actual: Date formatted WITH time
```

### Expected behavior

When `withTime={true}` is passed, the hidden input should contain the date value formatted with time information. When `withTime={false}` or when the prop is omitted, the time portion should be excluded from the formatted value.

The behavior seems to be inverted from what the prop name suggests.

### System Info

- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
