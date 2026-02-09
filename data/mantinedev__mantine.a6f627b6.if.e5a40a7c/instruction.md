# Bug Report

### Describe the bug

I'm experiencing an issue with the PinInput component where keyboard navigation between input fields is not working as expected. When I type in a pin input field, the focus should automatically move to the next field, but instead it seems like the default behavior is being prevented even when `manageFocus` is disabled.

### Reproduction

```jsx
import { PinInput } from '@mantine/core';

function Demo() {
  return (
    <PinInput 
      length={4} 
      manageFocus={false}
    />
  );
}
```

### Steps to reproduce:
1. Create a PinInput component with `manageFocus={false}`
2. Type a digit in the first input field
3. Notice that the focus doesn't move naturally - the default keyboard behavior seems to be blocked

### Expected behavior

When `manageFocus` is set to `false`, the component should not interfere with default keyboard navigation. The focus management should only be active when `manageFocus` is `true` (or not specified, if that's the default).

Currently it seems like the behavior is inverted - focus management is being prevented when it should be allowed, and vice versa.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
