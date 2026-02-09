# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props in Mantine components. When I try to use object-based responsive values (like `{ base: value1, sm: value2 }`), the styles are not being applied correctly. It seems like the responsive breakpoint values are being ignored completely.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
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

When using the component above, the padding and margin values don't change based on the breakpoint. The styles either don't apply at all or only use a default value.

### Expected behavior

The Box component should apply different padding/margin values at different breakpoints as specified in the object. For example:
- At base breakpoint: padding should be 'xs' and margin should be 10
- At sm breakpoint: padding should be 'md'
- At md breakpoint: margin should be 20
- At lg breakpoint: padding should be 'xl'

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome/Firefox

This was working fine before, but seems to have broken recently. Any help would be appreciated!

---
Repository: /testbed
