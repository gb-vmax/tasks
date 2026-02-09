# Bug Report

### Describe the bug

The `Mark` component is not applying theme colors correctly. When I pass a theme color (like `blue`, `red`, etc.) to the `color` prop, it's being treated as a custom color instead, and the background color isn't being applied from the theme.

### Reproduction

```jsx
import { Mark } from '@mantine/core';

function Demo() {
  return (
    <div>
      {/* This should use the theme color but doesn't work */}
      <Mark color="blue">Highlighted text</Mark>
      
      {/* This also doesn't apply the theme color */}
      <Mark color="red">Another highlight</Mark>
    </div>
  );
}
```

### Expected behavior

When passing a theme color name to the `Mark` component, it should use the corresponding color from the Mantine theme. The background should be the appropriate shade of the theme color.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
