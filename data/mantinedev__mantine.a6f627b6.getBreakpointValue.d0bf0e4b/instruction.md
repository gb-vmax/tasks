# Bug Report

### Describe the bug

When using responsive style props with breakpoint objects, the styles are not being applied correctly. Instead of getting the value for a specific breakpoint, the entire object is being returned, which breaks the styling system.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function Demo() {
  return (
    <Box
      p={{ base: 'xs', sm: 'md', lg: 'xl' }}
      m={{ base: 10, md: 20 }}
    >
      Content
    </Box>
  );
}
```

The padding and margin values are not being applied at their respective breakpoints. The component seems to be receiving the entire breakpoint object instead of the individual values.

### Expected behavior

The Box component should apply `p="xs"` at the base breakpoint, `p="md"` at sm, and `p="xl"` at lg. Similarly for margin values. Each breakpoint should receive its corresponding value from the object.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
