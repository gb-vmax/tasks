# Bug Report

### Describe the bug

The `withProps` static method is not being detected on components. When trying to use components that should have the `withProps` function, it appears the method is missing or not accessible.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// Try to use withProps
const CustomButton = Button.withProps({ variant: 'filled' });

// withProps is undefined or not working as expected
```

### Expected behavior

Components should expose a static `withProps` function that can be used to create component variants with predefined props. The function should be accessible as a property on the component.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
