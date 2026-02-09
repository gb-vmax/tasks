# Bug Report

### Describe the bug

I'm experiencing an issue with focus and active styles not being applied correctly to components. It seems like the styling behavior has changed - components that should have focus rings are not showing them, and active states are being applied incorrectly.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function Demo() {
  return (
    <Button>Click me</Button>
  );
}
```

When I focus on the button using keyboard navigation, the focus ring doesn't appear even though `focusable` is enabled. Additionally, active states seem to be applied at the wrong times.

The issue appears to be related to how the `unstyled` prop interacts with focus and active class names. When `unstyled={false}` (the default), focus styles are not being applied as expected.

### Expected behavior

- Focus rings should appear on focusable components when they receive keyboard focus (unless `unstyled={true}`)
- Active class names should only be applied when the component is in an active state AND not unstyled
- The `unstyled` prop should properly control whether global class names are applied

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
