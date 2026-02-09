# Bug Report

### Describe the bug

I'm experiencing an issue with the `lineHeight` style prop when using theme values. When I try to use a line height value that exists in my theme configuration (like `'xs'`, `'sm'`, `'md'`, etc.), it's not being applied correctly. Instead, the CSS variable reference is being generated even when the value doesn't exist in the theme.

### Reproduction

```jsx
import { Box, MantineProvider } from '@mantine/core';

const theme = {
  lineHeights: {
    xs: '1.4',
    sm: '1.55',
    md: '1.6',
  }
};

function App() {
  return (
    <MantineProvider theme={theme}>
      {/* This should use the theme value but doesn't work */}
      <Box lh="md">
        Some text with medium line height
      </Box>
      
      {/* This also has unexpected behavior */}
      <Box lh="xl">
        Some text with xl line height
      </Box>
    </MantineProvider>
  );
}
```

### Expected behavior

When using a line height value that exists in `theme.lineHeights` (like `'md'`), it should generate the correct CSS variable reference `var(--mantine-line-height-md)`. When using a value that doesn't exist in the theme, it should either pass through the value as-is or handle it differently.

Currently it seems like the logic is inverted - values that ARE in the theme don't get the CSS variable, while values that AREN'T in the theme do get it.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
