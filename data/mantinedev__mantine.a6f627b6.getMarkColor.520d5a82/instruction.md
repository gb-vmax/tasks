# Bug Report

### Describe the bug

When using the `Mark` component with a custom color (non-theme color), the background color is not being applied correctly. Instead of showing the expected color, the component displays a CSS variable string or incorrect color value.

### Reproduction

```jsx
import { Mark } from '@mantine/core';

// Using a custom hex color
<Mark color="#ff6b6b">Highlighted text</Mark>

// Or using rgb
<Mark color="rgb(255, 107, 107)">Highlighted text</Mark>
```

### Expected behavior

The `Mark` component should display the custom color as the background. When passing a non-theme color like `#ff6b6b`, it should apply that exact color value to the background.

### Actual behavior

The background color is not rendered properly - it appears to be using an incorrect CSS variable or the color is not being applied at all.

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
