# Bug Report

### Describe the bug

I'm experiencing an issue with variant class names being applied incorrectly when using the `unstyled` prop. It seems like variant classes are now being added even when `unstyled={true}` is set, which shouldn't happen.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This button should not have any variant classes applied
<Button unstyled variant="filled">
  Click me
</Button>

// Expected: No variant class in the output
// Actual: The variant class is still being applied
```

When inspecting the element, I can see that the variant class (e.g., `button--filled`) is present in the className even though `unstyled` is set to `true`.

### Expected behavior

When `unstyled={true}` is passed to a component, variant-specific classes should not be applied regardless of what `variant` prop is set. The `unstyled` prop should completely remove all default styling including variant styles.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
