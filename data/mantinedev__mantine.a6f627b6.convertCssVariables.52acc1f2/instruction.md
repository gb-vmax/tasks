# Bug Report

### Describe the bug

The color scheme CSS variables are being applied with inverted logic. When setting `data-mantine-color-scheme="dark"`, the light theme styles are being applied instead, and vice versa. This causes components to render with the wrong color scheme.

### Reproduction

```jsx
import { MantineProvider } from '@mantine/core';

function App() {
  return (
    <MantineProvider>
      <div data-mantine-color-scheme="dark">
        {/* This div should have dark theme styles but gets light theme instead */}
        <Button>Click me</Button>
      </div>
    </MantineProvider>
  );
}
```

### Expected behavior

When `data-mantine-color-scheme="dark"` is set, dark theme CSS variables should be applied. When `data-mantine-color-scheme="light"` is set, light theme CSS variables should be applied.

### Current behavior

The color schemes are reversed - dark attribute applies light styles and light attribute applies dark styles.

### System Info
- @mantine/core version: latest
- Browser: All browsers

---
Repository: /testbed
