# Bug Report

### Describe the bug

When passing `undefined` as a style prop, the component throws an error or behaves unexpectedly. This seems to have started happening recently - previously `undefined` styles were handled gracefully and just ignored.

### Reproduction

```jsx
import { Box } from '@mantine/core';

function MyComponent() {
  const conditionalStyle = condition ? { color: 'red' } : undefined;
  
  return <Box style={conditionalStyle}>Content</Box>;
}
```

When `condition` is false and `conditionalStyle` is `undefined`, the component doesn't handle it properly anymore.

### Expected behavior

Components should gracefully handle `undefined` style values and treat them as no styles applied (empty object). This is a common pattern when conditionally applying styles.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
