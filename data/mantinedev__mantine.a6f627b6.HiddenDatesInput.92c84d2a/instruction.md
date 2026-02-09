# Bug Report

### Describe the bug

I'm experiencing an issue with the `HiddenDatesInput` component where the `withTime` prop behavior seems to be inverted when a `type` prop is provided. When I set `withTime={true}` along with a `type`, the hidden input doesn't include time information in its value, and vice versa.

### Reproduction

```tsx
import { HiddenDatesInput } from '@mantine/dates';

const date = new Date('2024-01-15T14:30:00');

// This should include time but doesn't
<HiddenDatesInput 
  value={date} 
  type="range"
  withTime={true}
  name="datetime"
/>

// This should NOT include time but does
<HiddenDatesInput 
  value={date} 
  type="range"
  withTime={false}
  name="date"
/>
```

### Expected behavior

When `withTime={true}` is set, the hidden input value should include time information regardless of whether a `type` prop is provided. When `withTime={false}`, time should be excluded from the formatted value.

### System Info

- @mantine/dates version: latest
- React version: 18.x

This seems like the boolean logic for `withTime` might be getting flipped somewhere when used together with the `type` prop.

---
Repository: /testbed
