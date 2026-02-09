# Bug Report

### Describe the bug

I'm experiencing an issue with the NumberInput component where the increment button becomes disabled when the input field is empty. This prevents users from incrementing from an empty state, which is unexpected behavior.

### Reproduction

```jsx
import { NumberInput } from '@mantine/core';

function Demo() {
  return (
    <NumberInput 
      placeholder="Enter a number"
      defaultValue={undefined}
    />
  );
}
```

Steps to reproduce:
1. Render a NumberInput with no initial value (empty input)
2. Try to click the increment button
3. The button appears to be disabled and clicking it does nothing

### Expected behavior

The increment button should be enabled when the input is empty, allowing users to start incrementing from an empty state (which should probably increment to 0 or 1). This is standard behavior in most number input implementations.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
