# Bug Report

### Describe the bug

After updating to the latest version, the `withProps` method is now requiring all component props to be provided, even optional ones. This breaks existing code where we only want to override a subset of props.

### Reproduction

```tsx
import { Button } from '@mantine/core';

// This used to work but now throws a type error
const CustomButton = Button.withProps({
  variant: 'filled'
});

// TypeScript complains that other props like 'size', 'color', etc. are required
// even though they should be optional
```

### Expected behavior

The `withProps` method should accept partial props, allowing us to override only the props we want while keeping others optional. This is the intended use case for creating component variants with preset configurations.

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x
- React version: 18.x

---
Repository: /testbed
