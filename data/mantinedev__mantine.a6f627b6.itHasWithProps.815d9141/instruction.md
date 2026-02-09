# Bug Report

### Describe the bug

The `withProps` static function is not accessible on components. When trying to use `Component.withProps()`, I'm getting an error that `withProps` is not a function.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// This throws an error
const CustomButton = Button.withProps({
  variant: 'filled',
  color: 'blue'
});
```

### Expected behavior

`withProps` should be a static function available directly on the component, allowing us to create component variants with pre-defined props.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
