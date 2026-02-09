# Bug Report

### Describe the bug

When passing an array of `classNames` to a Mantine component, the styling breaks completely. Instead of merging multiple classNames objects as expected, the component seems to ignore or incorrectly process the array.

### Reproduction

```tsx
import { Button } from '@mantine/core';

const customClassNames = [
  { root: 'custom-root-1' },
  { root: 'custom-root-2' }
];

// This doesn't work correctly
<Button classNames={customClassNames}>
  Click me
</Button>
```

When using an array of classNames objects, the expected behavior would be to merge all the class names together. However, the component doesn't apply the styles properly.

Also noticed that when passing a single classNames object (non-array), it's not being applied either:

```tsx
const singleClassNames = { root: 'my-custom-class' };

// This also seems broken
<Button classNames={singleClassNames}>
  Click me
</Button>
```

### Expected behavior

- Array of classNames objects should be merged and all classes applied to the component
- Single classNames object should work as before
- The component should render with the correct CSS classes

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This seems like a regression as it was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
