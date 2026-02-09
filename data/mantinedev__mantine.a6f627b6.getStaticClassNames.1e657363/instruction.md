# Bug Report

### Describe the bug

Static class names are not being generated correctly for components. When using the styles API, the expected class names with the proper prefix format are missing from the DOM elements.

### Reproduction

```tsx
import { Button } from '@mantine/core';

function Demo() {
  return <Button>Click me</Button>;
}
```

When inspecting the DOM, the button element should have class names following the pattern `mantine-Button-root` (or similar with the configured prefix), but these static class names are either missing entirely or not formatted correctly.

### Expected behavior

Components should receive static class names in the format `{prefix}-{componentName}-{selector}` (e.g., `mantine-Button-root`, `mantine-Input-wrapper`, etc.) when `withStaticClass` is not explicitly set to `false`.

These class names are important for:
- Targeting elements with custom CSS
- Testing and automation selectors
- Debugging component structure

### System Info

- @mantine/core version: 7.x
- React version: 18.x

---
Repository: /testbed
