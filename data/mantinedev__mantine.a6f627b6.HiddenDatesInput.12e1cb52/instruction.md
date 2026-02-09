# Bug Report

### Describe the bug

The `HiddenDatesInput` component is rendering a visible input field instead of a hidden one, and the time portion of datetime values is being incorrectly included/excluded in the formatted output.

### Reproduction

```jsx
import { HiddenDatesInput } from '@mantine/dates';

function MyForm() {
  const dateValue = new Date('2024-01-15T14:30:00');
  
  return (
    <form>
      <HiddenDatesInput 
        value={dateValue}
        type="range"
        withTime={true}
        name="myDate"
      />
    </form>
  );
}
```

### Expected behavior

1. The input should have `type="hidden"` to keep it hidden from the UI
2. When `withTime={true}` is passed, the formatted value should include the time portion
3. When `withTime={false}` is passed, the formatted value should exclude the time portion

### Actual behavior

1. The input is visible in the form (uses the `type` prop value instead of "hidden")
2. The time formatting behavior is inverted - when `withTime={true}`, time is excluded, and when `withTime={false}`, time is included

This is affecting our form submissions as the hidden date inputs are now showing up in the UI and the datetime values are being formatted incorrectly.

---
Repository: /testbed
