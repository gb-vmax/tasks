# Bug Report

### Describe the bug

When using `withProps` on Mantine components, I'm getting a syntax error. It looks like there's a problem with the TypeScript type definition - the code won't even compile.

### Reproduction

```tsx
import { Button } from '@mantine/core';

const CustomButton = Button.withProps({
  variant: 'filled',
  color: 'blue'
});

// TypeScript compilation fails with syntax error
```

### Expected behavior

The component should compile successfully and `withProps` should work as documented, allowing me to create a component variant with pre-defined props.

### System Info
- @mantine/core version: latest
- TypeScript version: 5.x
- Node version: 18.x

---
Repository: /testbed
