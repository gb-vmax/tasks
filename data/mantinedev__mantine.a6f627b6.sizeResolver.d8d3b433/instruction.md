# Bug Report

### Describe the bug

I'm experiencing an issue with size props when passing numeric values to components. It seems like numeric size values are no longer being converted to rem units as expected.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// This should convert 16 to rem units but doesn't work
<Box w={16} h={32}>
  Content
</Box>

// String values like '16px' work fine
<Box w="16px" h="32px">
  Content
</Box>
```

When I pass a number like `16` or `32` to width/height props, the styles aren't being applied correctly. It looks like the numeric values aren't being processed at all.

### Expected behavior

Numeric values passed to size props (width, height, etc.) should be automatically converted to rem units. For example, `w={16}` should result in `width: 1rem` being applied.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
