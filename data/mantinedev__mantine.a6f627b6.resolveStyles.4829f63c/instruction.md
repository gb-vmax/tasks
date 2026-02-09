# Bug Report

### Describe the bug

When passing an array of styles to a Mantine component, only the last style in the array is being applied. It seems like styles from earlier array elements are being completely ignored instead of being merged together.

### Reproduction

```tsx
import { Button } from '@mantine/core';

<Button
  styles={[
    { root: { backgroundColor: 'red' } },
    { root: { color: 'white' } },
    { root: { padding: '20px' } }
  ]}
>
  Click me
</Button>
```

### Expected behavior

All styles from the array should be merged together, so the button should have:
- Red background
- White text color  
- 20px padding

### Actual behavior

Only the padding from the last object is applied. The backgroundColor and color from earlier array elements are lost.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
