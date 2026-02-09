# Bug Report

### Describe the bug

The Rating component's star symbols are displaying incorrectly. Empty/unfilled stars are showing as filled, and filled stars are showing as empty. The visual state of the stars is completely inverted from what it should be.

### Reproduction

```jsx
import { Rating } from '@mantine/core';

function Demo() {
  return <Rating defaultValue={3} />;
}
```

When rendering a Rating component with a value of 3, the first 3 stars should appear filled, but instead they appear empty, and the remaining stars appear filled.

### Expected behavior

Stars should be filled up to the current rating value. For example:
- Rating value of 3 out of 5 → first 3 stars filled, last 2 empty
- Rating value of 0 → all stars empty
- Rating value of 5 → all stars filled

Currently, the behavior is reversed - empty stars are rendered as filled and vice versa.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
