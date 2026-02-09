# Bug Report

### Describe the bug

The `dimmed` color is not respecting the color scheme anymore. When using `color="dimmed"` in dark mode, it's now showing the same color as light mode instead of using the appropriate dark mode variant.

Also, theme colors without an explicit shade are using the wrong shade based on the current color scheme - it seems like the logic is inverted.

### Reproduction

```jsx
import { MantineProvider, Text } from '@mantine/core';

function App() {
  return (
    <MantineProvider theme={{ colorScheme: 'dark' }}>
      <Text color="dimmed">This should be dark[2] in dark mode</Text>
      <Text color="blue">This should use the light primary shade in dark mode</Text>
    </MantineProvider>
  );
}
```

### Expected behavior

1. When `color="dimmed"` is used in dark mode, it should return `theme.colors.dark[2]`
2. When `color="dimmed"` is used in light mode, it should return `theme.colors.gray[7]`
3. When a theme color is used without a shade (e.g., `color="blue"`), it should use the primary shade that corresponds to the current color scheme (light shade for light mode, dark shade for dark mode)

### Current behavior

- `dimmed` always returns `gray[7]` regardless of color scheme
- Theme colors without explicit shades appear to be using the opposite color scheme's primary shade

This seems like a regression - the dimmed color used to adapt to the color scheme properly.

---
Repository: /testbed
