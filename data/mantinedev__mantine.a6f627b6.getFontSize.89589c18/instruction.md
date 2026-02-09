# Bug Report

### Describe the bug

The `getFontSize` utility is returning incorrect values. When I pass a font size value to `getFontSize`, I'm getting back an object instead of the actual size value. This is causing issues in components that rely on this utility function.

### Reproduction

```tsx
import { getFontSize } from '@mantine/core';

// This returns an object instead of the font size value
const fontSize = getFontSize('md');
console.log(fontSize); // Expected: '16px' or similar, Got: undefined or object
```

When using components that internally call `getFontSize`, the font sizes are not being applied correctly. The text appears with default browser styling instead of the expected Mantine theme font sizes.

### Expected behavior

`getFontSize` should return the actual font size value (string or number) that can be directly used in CSS, similar to how other size utilities like `getRadius` work.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
