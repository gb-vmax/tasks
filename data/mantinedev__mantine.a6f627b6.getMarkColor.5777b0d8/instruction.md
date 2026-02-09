# Bug Report

### Describe the bug

The `Mark` component is not applying colors correctly. When I pass a theme color to the `Mark` component, it's rendering with the raw color value instead of using the theme variable. Conversely, when I pass a custom color (non-theme color), it's trying to use a theme variable that doesn't exist.

### Reproduction

```jsx
import { Mark } from '@mantine/core';

// This should use the theme color variable but shows the raw color name instead
<Mark color="blue">Highlighted text</Mark>

// This should use the custom color directly but tries to use a theme variable
<Mark color="#ff6b6b">Custom color highlight</Mark>
```

### Expected behavior

- When using a theme color like `"blue"`, the component should apply the appropriate CSS variable (e.g., `var(--mantine-color-blue-5)`)
- When using a custom color like `"#ff6b6b"`, the component should apply that color directly without trying to convert it to a theme variable

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
