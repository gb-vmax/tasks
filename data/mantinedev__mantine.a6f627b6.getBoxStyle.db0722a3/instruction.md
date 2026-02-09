# Bug Report

### Describe the bug

I'm experiencing an issue with CSS variable styling in the Box component. When I apply both inline styles and CSS variables to a Box component, the CSS variables are being overridden by the inline styles instead of taking precedence.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      style={{ color: 'blue' }}
      vars={{ '--my-color': 'red' }}
    >
      Content
    </Box>
  );
}
```

In this example, I'd expect the CSS variables to be applied last so they can override the inline styles when needed, but they're being applied in the wrong order.

### Expected behavior

CSS variables (`vars` prop) should be applied after other style properties so they can properly override inline styles when necessary. The order of style application should be: base styles → inline styles → CSS variables.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
