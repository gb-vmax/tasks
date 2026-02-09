# Bug Report

### Describe the bug

The `fontFamily` style prop is not working correctly when using theme font family keys. When I pass a valid font family key like `'monospace'` or `'heading'`, it's being treated as a literal string instead of resolving to the corresponding theme font family value.

### Reproduction

```tsx
import { Box } from '@mantine/core';

// This should use the theme's monospace font but renders as literal "monospace"
<Box ff="monospace">
  This text should use the theme monospace font
</Box>

// Same issue with other font family keys
<Box ff="heading">
  This should use the theme heading font
</Box>
```

### Expected behavior

When passing theme font family keys (`'monospace'`, `'heading'`, `'text'`) to the `ff` prop, they should resolve to the actual font family values defined in the theme (e.g., `'ui-monospace, monospace'` for monospace).

Currently it seems like the font family resolver is just returning the string as-is instead of looking up the theme value.

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
