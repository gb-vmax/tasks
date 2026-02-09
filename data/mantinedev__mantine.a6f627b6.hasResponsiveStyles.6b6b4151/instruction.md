# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props when using array values. It seems like array-based style props are being treated as responsive objects when they shouldn't be, causing unexpected behavior in the styling system.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// Using an array value for a style prop
<Box style={{ padding: [10, 20, 30] }}>
  Content
</Box>

// Or with other array-based props
<Box m={[10, 20]}>
  Content  
</Box>
```

When passing arrays as style prop values, the component treats them as if they contain responsive breakpoint definitions, but they're just regular array values that should be passed through as-is.

### Expected behavior

Array values in style props should be handled correctly and not mistaken for responsive style objects. The styling should apply the array value directly without trying to parse it as a responsive configuration.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
