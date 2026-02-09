# Bug Report

### Describe the bug

When passing an array of style objects to a component, the styles are being applied in the wrong order. Later styles in the array are being overridden by earlier ones instead of the other way around.

### Reproduction

```tsx
import { Box } from '@mantine/core';

// The red background should take precedence, but blue is applied instead
<Box
  style={[
    { backgroundColor: 'blue', padding: '10px' },
    { backgroundColor: 'red' }
  ]}
>
  Content
</Box>
```

### Expected behavior

When using an array of styles, styles that appear later in the array should override earlier ones (similar to how CSS cascade works). In the example above, the box should have a red background, not blue.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
