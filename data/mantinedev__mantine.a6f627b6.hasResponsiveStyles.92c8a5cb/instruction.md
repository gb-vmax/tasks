# Bug Report

### Describe the bug

When passing `null` as a style prop value, the component crashes with a runtime error. It seems like `null` values are not being handled correctly in the responsive styles logic.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box style={{ padding: null }}>
      Content
    </Box>
  );
}
```

The component throws an error when trying to access properties on `null`.

### Expected behavior

The component should handle `null` values gracefully without crashing. `null` is a common value used to reset or clear styles conditionally.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
