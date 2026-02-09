# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props in Mantine components. When I pass an object with only a `base` property for styling, the styles are not being applied correctly. It seems like the responsive styles detection is not working as expected.

### Reproduction

```tsx
import { Box } from '@mantine/core';

// This doesn't work - styles are not applied
<Box p={{ base: 'md' }}>
  Content here
</Box>

// Also having issues with single breakpoint objects
<Box m={{ base: '10px' }}>
  More content
</Box>
```

The styles should be applied but they're being ignored. When I use a plain string value instead of an object, it works fine:

```tsx
// This works
<Box p="md">
  Content here
</Box>
```

### Expected behavior

When using an object with a `base` property for responsive styles, the styles should be applied to the component. The `base` breakpoint should work the same as passing a plain value.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
