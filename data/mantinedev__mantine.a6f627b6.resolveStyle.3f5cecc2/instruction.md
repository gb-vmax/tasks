# Bug Report

### Describe the bug

When passing a function to the `style` prop, the theme object is no longer being passed to the function. Instead, an empty object is being passed, which breaks any styles that depend on theme values.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      style={(theme) => ({
        backgroundColor: theme.colors.blue[5],
        padding: theme.spacing.md
      })}
    >
      Content
    </Box>
  );
}
```

In the above example, `theme.colors` and `theme.spacing` are undefined because the theme object is not being passed to the style function.

### Expected behavior

The style function should receive the theme object as its first argument, allowing access to theme colors, spacing, and other theme properties.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
