# Bug Report

### Describe the bug

I'm experiencing an issue with responsive style props where passing `null` as a style prop value causes the application to crash with a runtime error. This seems to be a regression as it was working fine in previous versions.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  const conditionalStyle = someCondition ? { base: '10px' } : null;
  
  return (
    <Box p={conditionalStyle}>
      Content here
    </Box>
  );
}
```

When `conditionalStyle` is `null`, the component throws an error trying to access properties on null.

### Expected behavior

The component should handle `null` style prop values gracefully without crashing. Passing `null` should be treated as "no style applied" and the component should render normally.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
