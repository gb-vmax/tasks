# Bug Report

### Describe the bug

The `getInputValue` helper function is returning incorrect values when trying to extract the current value from date input elements. Instead of getting the actual input value, I'm getting `null` or undefined results.

### Reproduction

```tsx
import { getInputValue } from '@mantine-tests/dates';

// Create a date input component
const container = render(<DateInput value={new Date()} />);

// Try to get the input value
const value = getInputValue(container.container);

// Expected: The formatted date string (e.g., "12/25/2023")
// Actual: null or undefined
```

### Expected behavior

The helper should correctly extract and return the value from the date input element, whether it's displayed as text content or stored as an attribute.

### System Info
- @mantine/dates version: latest
- Browser: Chrome/Firefox
- Testing library version: latest

---
Repository: /testbed
