# Bug Report

### Describe the bug

I'm experiencing an issue with the styles API where root class names are not being applied correctly to components. It seems like the logic for determining when to apply the root className has changed, and now it's behaving in the opposite way - the className is being applied when the selector is NOT the root, instead of when it IS the root.

### Reproduction

```tsx
import { useStyles } from '@mantine/core';

// When rootSelector equals selector (which should be the root case)
const result = getRootClassName({
  rootSelector: 'root',
  selector: 'root',
  className: 'my-class'
});

// Expected: 'my-class'
// Actual: undefined
```

The className is not being returned when the selector matches the rootSelector, which breaks the styling for root elements.

### Expected behavior

When `rootSelector === selector`, the function should return the `className` because that indicates we're styling the root element. Currently it's returning `undefined` in this case.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
