# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props when using object notation. It seems like the `base` property is not being handled correctly when I try to use object-based responsive values.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      p={{
        base: 'md',
        sm: 'lg',
        md: 'xl'
      }}
    >
      Content
    </Box>
  );
}
```

When using the above code, the base padding value doesn't seem to be applied correctly. The component should use `md` padding by default and scale up on larger breakpoints, but the base value appears to be ignored or filtered out incorrectly.

### Expected behavior

The `base` property should be treated as the default/mobile-first value and applied to the element. Other breakpoint keys (`sm`, `md`, `lg`, etc.) should override it at their respective screen sizes.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
