# Bug Report

### Describe the bug

When passing an array of style objects to a Mantine component, the first style object in the array is being ignored and not applied. Only styles from the second element onwards are being merged and rendered.

### Reproduction

```jsx
import { Box } from '@mantine/core';

const styles = [
  { color: 'red', fontSize: '16px' },
  { backgroundColor: 'blue' },
  { padding: '10px' }
];

<Box style={styles}>
  Content here
</Box>
```

### Expected behavior

All three style objects should be merged and applied to the Box component. The text should be red with 16px font size, have a blue background, and 10px padding.

### Actual behavior

The first style object (`{ color: 'red', fontSize: '16px' }`) is completely ignored. Only the background color and padding are applied. The text appears in the default color instead of red, and the font size is not changed.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
