# Bug Report

### Describe the bug
When passing responsive style props to Mantine components, the base value is not being extracted correctly and the styles are not applied as expected. It seems like objects with a `base` property are being ignored entirely.

### Reproduction
```tsx
import { Box } from '@mantine/core';

// This should use the base value 'red' but doesn't work
<Box bg={{ base: 'red', sm: 'blue' }}>
  Content
</Box>

// Regular values still work fine
<Box bg="red">
  Content
</Box>
```

The component with the responsive `bg` prop doesn't render with the expected base background color. The base value seems to be completely ignored and the background doesn't appear at all.

### Expected behavior
When using an object with a `base` property for responsive styles, the base value should be applied. The box should have a red background on all screen sizes, changing to blue on small screens and up.

### System Info
- @mantine/core version: latest
- Browser: Chrome 120
- OS: macOS

---
Repository: /testbed
