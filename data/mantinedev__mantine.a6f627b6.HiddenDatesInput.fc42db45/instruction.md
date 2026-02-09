# Bug Report

### Describe the bug

The `HiddenDatesInput` component is not working correctly when the `withTime` prop is set to `true`. The hidden input field seems to be formatting dates without time information even when `withTime={true}` is explicitly passed.

### Reproduction

```jsx
import { HiddenDatesInput } from '@mantine/dates';

// This should include time in the formatted value
<HiddenDatesInput
  value={new Date('2024-01-15T14:30:00')}
  type="default"
  name="dateField"
  form="myForm"
  withTime={true}
/>
```

When inspecting the rendered hidden input, the value doesn't contain the time portion even though `withTime` is set to `true`. It appears to be doing the opposite - when `withTime={true}`, it formats without time, and when `withTime={false}`, it includes the time.

### Expected behavior

When `withTime={true}` is passed, the hidden input should contain the formatted date WITH time information. When `withTime={false}`, it should format the date WITHOUT time information.

Also noticed that the `form` attribute seems to behave strangely - when a form ID is provided, it's not being set on the hidden input element.

### System Info
- @mantine/dates version: latest
- React version: 18.x

---
Repository: /testbed
