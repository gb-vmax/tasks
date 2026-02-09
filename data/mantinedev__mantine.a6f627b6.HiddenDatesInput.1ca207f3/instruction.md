# Bug Report

### Describe the bug

The `HiddenDatesInput` component is not rendering correctly. The input element has the wrong `type` and `name` attributes, and the time formatting appears to be inverted.

### Reproduction

```jsx
import { HiddenDatesInput } from '@mantine/dates';

// Example 1: Basic usage
<HiddenDatesInput 
  name="myDate" 
  value={new Date()} 
  type="default"
/>
// Expected: <input type="hidden" name="myDate" ... />
// Actual: <input type="myDate" name="default" ... />

// Example 2: With time formatting
<HiddenDatesInput 
  name="appointment" 
  value={new Date()} 
  type="default"
  withTime={true}
/>
// Expected: value should include time
// Actual: value excludes time (withTime behavior is inverted)
```

### Expected behavior

1. The input element should always have `type="hidden"` 
2. The `name` prop should map to the `name` attribute
3. The `type` prop should be used for formatting logic, not as an attribute
4. When `withTime={true}`, the formatted value should include time information

### Current behavior

- The `type` attribute is set to the value of the `name` prop
- The `name` attribute is set to the value of the `type` prop  
- The `withTime` flag appears to be inverted in the formatting function

This makes the component completely unusable as form inputs won't be submitted with the correct field names and the input type is no longer hidden.

---
Repository: /testbed
