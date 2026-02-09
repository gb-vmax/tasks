# Bug Report

### Describe the bug

When using the `MantineProvider` with forced color schemes, the dark and light mode CSS variables are being applied to the wrong color scheme. Setting `data-mantine-color-scheme="dark"` applies light mode styles and vice versa.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{ ... }}>
      <div data-mantine-color-scheme="dark">
        {/* This div should have dark mode styles but gets light mode styles instead */}
        <Button>Click me</Button>
      </div>
    </MantineProvider>
  );
}
```

Steps to reproduce:
1. Set up a component with `data-mantine-color-scheme="dark"`
2. Inspect the applied CSS variables
3. Notice that light mode variables are being applied instead of dark mode variables

### Expected behavior

When `data-mantine-color-scheme="dark"` is set, dark mode CSS variables should be applied. When `data-mantine-color-scheme="light"` is set, light mode CSS variables should be applied.

Currently experiencing the opposite behavior - the color schemes are swapped.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
