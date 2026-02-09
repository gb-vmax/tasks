# Bug Report

### Describe the bug

The `fontFamily` style prop is not working correctly. When I pass a valid font family value like `'monospace'` or `'text'`, it doesn't apply the expected font family from the theme. Instead, the component seems to be using an incorrect value.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box ff="monospace">
      This text should use the monospace font family from the theme
    </Box>
  );
}
```

When inspecting the rendered element, the font-family CSS property is not set to the expected theme value. The same issue occurs with other valid font family values like `'text'` and `'heading'`.

### Expected behavior

When using `ff="monospace"` (or any other valid font family key), the component should apply the corresponding font family value from the theme. For example, `'monospace'` should resolve to the monospace font family defined in the theme configuration.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
