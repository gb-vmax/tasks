# Bug Report

### Describe the bug

I'm experiencing an issue where styles are not being applied correctly to components. It seems like the root element styles are being ignored while nested element styles are being applied when they shouldn't be, or vice versa.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      style={{ backgroundColor: 'red' }}
    >
      Content
    </Box>
  );
}
```

When rendering this component, the `backgroundColor` style that should be applied to the root element is not showing up. However, if I inspect nested elements within more complex components, I see styles being applied that shouldn't be there.

### Expected behavior

- Root element styles should be applied to the root selector
- Nested element styles should only be applied to their respective selectors
- The style prop should work as expected on the main component element

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to have started happening recently. The styling system appears to have the selectors inverted or something similar.

---
Repository: /testbed
