# Bug Report

### Describe the bug

The `fontFamily` style prop is not resolving correctly when using theme font family values. When I pass a valid font family key like `'monospace'` or `'text'`, the component doesn't apply the correct font family from the theme.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <>
      <Box ff="monospace">This should use monospace font</Box>
      <Box ff="text">This should use text font</Box>
    </>
  );
}
```

### Expected behavior

When using `ff="monospace"` or `ff="text"`, the Box component should resolve these to the actual font family values defined in the theme (e.g., `ui-monospace, SFMono-Regular, ...` for monospace). Instead, it seems to be returning the string literal rather than the resolved theme value.

### System Info

- @mantine/core version: latest
- Browser: Chrome
- OS: macOS

---
Repository: /testbed
