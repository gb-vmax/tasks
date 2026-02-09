# Bug Report

### Describe the bug

The `fontFamily` style prop is not resolving correctly when using predefined theme font family values. When I pass a valid font family key like `'monospace'` or `'heading'`, the component doesn't apply the correct font family from the theme.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should use the monospace font from theme
<Box ff="monospace">
  This text should be monospace
</Box>

// This should use the heading font from theme  
<Box ff="heading">
  This text should use heading font
</Box>
```

### Expected behavior

When using predefined font family keys (`'monospace'`, `'text'`, `'heading'`), the component should resolve these to the actual font family values defined in the theme configuration. Instead, it seems like the font family is not being applied at all or is being applied incorrectly.

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
