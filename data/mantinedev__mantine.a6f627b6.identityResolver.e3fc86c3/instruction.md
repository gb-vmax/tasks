# Bug Report

### Describe the bug

I'm experiencing an issue with style props when passing `undefined` values to Box components. The component seems to be rendering `undefined` as a string in the DOM instead of ignoring it or treating it as null.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  const dynamicMargin = undefined;
  
  return (
    <Box m={dynamicMargin}>
      Content here
    </Box>
  );
}
```

When inspecting the rendered element, I'm seeing `undefined` appear in the styles or attributes instead of being properly handled.

### Expected behavior

When a style prop value is `undefined`, it should either:
- Be ignored completely and not render any style
- Be converted to `null` so it doesn't appear in the output

The component shouldn't render the literal string "undefined" in the DOM.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
