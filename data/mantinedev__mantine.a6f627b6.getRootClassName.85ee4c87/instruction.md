# Bug Report

### Describe the bug

I'm experiencing an issue with className handling in styled components. When applying custom classNames to root elements, they're not being applied correctly anymore. Instead, it seems like the className logic has been inverted - classNames are being added to non-root selectors when they should only be on the root selector.

### Reproduction

```jsx
import { Box } from '@mantine/core';

// Custom className should be applied to root element
<Box className="my-custom-class">
  Content
</Box>
```

When inspecting the DOM, the custom className appears on child elements or is missing entirely from the root element where it should be applied.

### Expected behavior

The `className` prop should be applied to the root element of the component. Non-root selectors should not receive the root className.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems to have broken after a recent update. The className application logic appears to be reversed from what it should be.

---
Repository: /testbed
