# Bug Report

### Describe the bug
When using style props with `null` values in the Box component, the application crashes with an error. It seems like the style prop parser doesn't handle `null` values correctly when checking for object types.

### Reproduction
```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box
      style={{
        margin: null,
        padding: null
      }}
    >
      Content
    </Box>
  );
}
```

Or when using responsive style props:

```jsx
<Box m={null} p={null}>
  Content
</Box>
```

### Expected behavior
The component should handle `null` values gracefully without crashing. Either ignore them or treat them as no value set.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
