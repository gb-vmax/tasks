# Bug Report

### Describe the bug

The static class names generated for components are using the wrong order for the class name segments. The current implementation puts the theme name after the selector, but it should be before the selector.

### Reproduction

```tsx
import { useStyles } from '@mantine/core';

// When using a component with static class names
// Expected: mantine-Button-root
// Actual: mantine-root-Button

const Component = () => {
  // The generated class names have selector and theme name swapped
  // This breaks CSS targeting and existing styles that depend on the correct class name format
  return <Button>Click me</Button>;
};
```

### Expected behavior

Static class names should follow the pattern: `{prefix}-{themeName}-{selector}`

For example:
- `mantine-Button-root`
- `mantine-Modal-overlay`
- `mantine-Input-wrapper`

### Current behavior

The class names are being generated in the wrong order: `{prefix}-{selector}-{themeName}`

This breaks existing CSS selectors and styling that rely on the correct class name structure.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
