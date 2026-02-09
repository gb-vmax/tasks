# Bug Report

### Describe the bug

The filled hover state for color variables is showing a lighter shade instead of a darker shade when hovering over filled components. This makes the hover effect appear incorrect - buttons and other filled components get lighter on hover instead of darker.

### Reproduction

```tsx
import { Button, MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <MantineProvider>
      <Button color="blue" variant="filled">
        Hover over me
      </Button>
    </MantineProvider>
  );
}
```

When hovering over the button, the color becomes lighter instead of darker. The expected behavior is that the hover state should be a darker shade than the base filled color.

### Expected behavior

Filled variant components should darken on hover, not lighten. For example, if a button uses shade 6 as the base color, hovering should use shade 7 (darker), not shade 5 (lighter).

### Additional context

This also affects the `light-color` variant - the text color contrast seems off compared to previous versions. The color being used appears to be one shade off from what it should be.

---
Repository: /testbed
