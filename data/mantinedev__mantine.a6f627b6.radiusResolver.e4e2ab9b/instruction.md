# Bug Report

### Describe the bug

I'm experiencing issues with the `radius` prop on Box components. When I pass theme radius values (like `'sm'`, `'md'`, `'lg'`), they're not being applied correctly. Instead, the component seems to be treating them as custom values.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <>
      {/* This should use theme.radius.sm but doesn't work */}
      <Box radius="sm" style={{ border: '1px solid red' }}>
        Small radius
      </Box>
      
      {/* This should use theme.radius.md but doesn't work */}
      <Box radius="md" style={{ border: '1px solid red' }}>
        Medium radius
      </Box>
    </>
  );
}
```

When inspecting the rendered elements, the CSS variable `--mantine-radius-sm` is being applied even though `'sm'` exists in `theme.radius`. It seems like the radius resolver is doing the opposite of what it should - applying CSS variables for theme values instead of returning them directly.

Additionally, when passing numeric values like `radius={16}`, nothing gets applied at all. The function seems to execute but doesn't return anything.

### Expected behavior

- When passing theme radius keys (`'sm'`, `'md'`, `'lg'`, etc.), the component should use the corresponding CSS variable from the theme
- When passing numeric values, they should be converted to rem units and applied
- The border radius should actually be visible on the rendered elements

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
