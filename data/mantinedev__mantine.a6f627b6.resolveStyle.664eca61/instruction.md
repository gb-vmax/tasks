# Bug Report

### Describe the bug

When passing an array of styles to a Mantine component, the styles are being applied in the wrong order. The last style in the array should have the highest priority (overriding previous styles), but instead the first style is taking precedence.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// Expected: background should be 'blue' (last item in array)
// Actual: background is 'red' (first item in array)
<Box 
  style={[
    { background: 'red', padding: '10px' },
    { background: 'blue' }
  ]}
>
  Content
</Box>
```

The background ends up being red instead of blue. The last style object in the array should override the previous ones, similar to how CSS cascade works.

### Expected behavior

When multiple style objects are provided in an array, later styles should override earlier ones. This is the standard behavior for style composition in React and other frameworks.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
