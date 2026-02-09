# Bug Report

### Describe the bug

The Rating component's star symbols are displaying incorrectly - empty stars are showing as filled and filled stars are showing as empty. The visual state of the stars is inverted from what it should be.

### Reproduction

```jsx
import { Rating } from '@mantine/core';

function Demo() {
  return <Rating defaultValue={3} />;
}
```

When rendering a Rating component with a value of 3, the first 3 stars should appear filled, but instead they appear empty and the remaining stars appear filled.

### Expected behavior

Stars with values less than or equal to the rating value should be displayed as filled. Stars with values greater than the rating value should be displayed as empty.

For example, with `defaultValue={3}`:
- Stars 1, 2, 3 should be filled
- Stars 4, 5 should be empty

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
