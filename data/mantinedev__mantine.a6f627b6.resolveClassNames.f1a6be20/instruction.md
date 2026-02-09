# Bug Report

### Describe the bug

When passing an array of `classNames` to a Mantine component, the styles are not being applied correctly. It seems like array classNames are being wrapped in an additional array layer, causing the styling system to malfunction.

### Reproduction

```jsx
import { Button } from '@mantine/core';

const customClassNames = [
  { root: 'custom-root-1' },
  { root: 'custom-root-2' }
];

// This doesn't work as expected
<Button classNames={customClassNames}>
  Click me
</Button>
```

When providing an array of classNames objects, the component doesn't receive the correct styling. It appears that the array is being treated incorrectly in the internal resolution logic.

### Expected behavior

The component should properly merge all classNames from the array and apply them to the respective elements. Each object in the array should contribute its class names to the final result.

### System Info

- @mantine/core version: 7.x
- React version: 18.x
- Browser: Chrome 121

---
Repository: /testbed
