# Bug Report

### Describe the bug

I'm experiencing an issue with focus and active class names not being applied correctly to components. It seems like the logic for determining when to apply these global class names has changed unexpectedly.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// Case 1: Focusable component with unstyled prop
<Button focusable unstyled>
  Click me
</Button>
// Expected: No focus ring classes should be applied
// Actual: Focus ring classes are being applied

// Case 2: Active component without unstyled
<Button active>
  Active button
</Button>
// Expected: Active class should be applied
// Actual: Active class is not applied
```

### Expected behavior

- When `unstyled` is true, global class names (focus ring, active styles) should not be applied
- When `focusable` is true and `unstyled` is false, focus ring classes should be applied
- When `active` is true and `unstyled` is false, active class should be applied

### Current behavior

The focus and active class names seem to be applied in the opposite scenarios or not at all. Components that should have focus rings don't get them, and components that shouldn't have them do.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: All browsers

---
Repository: /testbed
