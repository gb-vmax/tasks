# Bug Report

### Describe the bug

The `Mark` component is not rendering the correct background color when using theme colors without specifying a shade. When I pass a color like `"blue"` without a shade number, the component doesn't display any background color or displays incorrectly.

### Reproduction

```jsx
import { Mark } from '@mantine/core';

function Demo() {
  return (
    <div>
      <Mark color="blue">This should have a blue background</Mark>
      <Mark color="red">This should have a red background</Mark>
    </div>
  );
}
```

### Expected behavior

When using a theme color without a specific shade (e.g., `color="blue"`), the `Mark` component should apply the default shade for that color and display the appropriate background color. The text should be highlighted with the theme's default blue/red color.

### System Info

- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
