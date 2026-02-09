# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props in Mantine components. When I try to use breakpoint-based styling with object notation, the styles are not being applied at all. The component seems to ignore the responsive values completely.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      p={{ base: 'md', sm: 'lg', md: 'xl' }}
      m={{ base: 10, sm: 20 }}
    >
      Content here
    </Box>
  );
}
```

When I render this component, none of the responsive padding or margin values are applied. The Box renders without any spacing styles.

This also happens with other style props like `w`, `h`, `bg`, etc. when using the object notation for breakpoints.

### Expected behavior

The component should apply the style values based on the current breakpoint. For example, at the `base` breakpoint it should use `md` padding, at `sm` it should use `lg` padding, and so on.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
