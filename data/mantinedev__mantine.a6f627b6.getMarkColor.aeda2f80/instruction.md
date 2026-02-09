# Bug Report

### Describe the bug

The `Mark` component is not correctly handling color shades when using theme colors. When I specify a color with a shade (like `blue.5`), it seems to be using the default shade instead of the one I provided. Conversely, when I don't specify a shade and expect the default to be used, it's not working as expected.

### Reproduction

```jsx
import { Mark } from '@mantine/core';

// This should use shade 5 but appears to use the default shade instead
<Mark color="blue.5">Highlighted text</Mark>

// This should use the default shade but doesn't render correctly
<Mark color="blue">Highlighted text</Mark>
```

### Expected behavior

- When a color with a specific shade is provided (e.g., `blue.5`), the Mark component should use that exact shade
- When only a color name is provided without a shade (e.g., `blue`), it should fall back to the default shade
- The component should correctly resolve the CSS variable for the specified color/shade combination

### System Info
- @mantine/core version: latest
- Browser: Chrome 120

---
Repository: /testbed
