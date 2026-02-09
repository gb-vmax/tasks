# Bug Report

### Describe the bug

When passing an array of styles to a component, only the first style object in the array is being applied. The subsequent styles in the array are being ignored completely.

### Reproduction

```tsx
import { Box } from '@mantine/core';

const styles = [
  { backgroundColor: 'red' },
  { color: 'white' },
  { padding: '20px' }
];

<Box styles={styles}>
  Content
</Box>
```

In this example, only `backgroundColor: 'red'` is applied, while `color: 'white'` and `padding: '20px'` are not being merged into the final styles.

### Expected behavior

All style objects in the array should be merged together and applied to the component. Each subsequent style should override any conflicting properties from previous styles.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
