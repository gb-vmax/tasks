# Bug Report

### Describe the bug

When passing an array of style objects to the `style` prop, the styles are being applied in the wrong order. The last style in the array should have the highest priority and override previous styles, but currently earlier styles are overriding later ones.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// The second style object should override the first one
<Box
  style={[
    { color: 'red', fontSize: 16 },
    { color: 'blue' }
  ]}
>
  Text
</Box>
```

### Expected behavior

The text should be blue (from the second style object), but it appears red instead. When multiple style objects are provided in an array, later styles should take precedence over earlier ones, similar to how CSS cascade works.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
