# Bug Report

### Describe the bug

When passing style props with responsive breakpoint values to Box component, the styles are not being applied correctly. The component seems to ignore object values for responsive styles and only applies the base styles.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      p={{ base: 'sm', md: 'lg', xl: 'xl' }}
      m={{ base: 10, sm: 20, lg: 30 }}
    >
      Content here
    </Box>
  );
}
```

When rendering this component, the padding and margin values for different breakpoints are not being applied. Only the default/base styles seem to work.

### Expected behavior

The Box component should apply different padding and margin values at different breakpoints as specified in the object notation. For example, padding should be 'sm' on mobile, 'lg' on medium screens, and 'xl' on extra large screens.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
