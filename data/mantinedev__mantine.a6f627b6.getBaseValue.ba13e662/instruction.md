# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props in Mantine components. When I pass an object with a `base` property for responsive styling, the base value is not being applied correctly. Instead, the entire object seems to be used as the value, which results in incorrect styling.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      p={{ base: 'md', sm: 'lg' }}
    >
      Content
    </Box>
  );
}
```

In this example, the padding should use `'md'` as the base value and `'lg'` for small screens and up. However, the base value doesn't seem to be extracted properly from the object.

### Expected behavior

The component should apply the `base` value from the responsive style object. In the example above, the padding should be `'md'` at the base breakpoint.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
