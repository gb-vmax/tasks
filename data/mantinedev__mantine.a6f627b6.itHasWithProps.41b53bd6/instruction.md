# Bug Report

### Describe the bug

The `withProps` static method on components is not being recognized correctly. When checking if a component has the `withProps` functionality, the type validation is failing.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This should work but doesn't
const CustomButton = Button.withProps({ variant: 'filled' });

// The withProps method exists but type checking fails
console.log(typeof Button.withProps); // Expected: 'function', but validation expects 'object'
```

### Expected behavior

The `withProps` static method should be recognized as a function and work properly for creating component variants with preset props.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
