# Bug Report

### Describe the bug

The `withProps` static method is not being recognized correctly on components. When trying to use components with the `withProps` functionality, it appears the method is not accessible or not working as expected.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// Trying to use withProps
const CustomButton = Button.withProps({
  variant: 'filled',
  color: 'blue'
});

// withProps doesn't seem to be available or working
```

### Expected behavior

Components should have a static `withProps` function that can be called to create a component with default props. The function should be accessible and work correctly to allow creating customized versions of components.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
