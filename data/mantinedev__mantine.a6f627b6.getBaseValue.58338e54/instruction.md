# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props in Mantine components. When I try to use an object with a `base` property for responsive styling, the base value is not being applied correctly to the component.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      style={{
        padding: {
          base: '10px',
          sm: '20px',
          md: '30px'
        }
      }}
    >
      Content here
    </Box>
  );
}
```

### Expected behavior

The component should use the `base` value ('10px' padding in this case) as the default, and then apply responsive values at different breakpoints. However, the base value doesn't seem to be getting extracted or applied at all.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
