# Bug Report

### Describe the bug

The hover state for filled variant buttons/components is showing the wrong color shade. When hovering over a filled button, it's getting lighter instead of darker, which looks really off visually.

### Reproduction

```jsx
import { Button, MantineProvider } from '@mantine/core';

function Demo() {
  return (
    <MantineProvider>
      <Button variant="filled" color="blue">
        Hover over me
      </Button>
    </MantineProvider>
  );
}
```

When you hover over the button, the color becomes lighter (goes to a lower shade number) instead of darker (higher shade number). For example, if the base color is shade 6, hovering makes it shade 5 instead of shade 7.

Also noticed that the light variant text color seems wrong - it's using a shade that's too dark in light mode and doesn't have enough contrast.

### Expected behavior

- Filled variant hover should use a darker shade (higher number) than the base color
- Light variant text color should use an appropriate shade for the color scheme

### System Info

- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
