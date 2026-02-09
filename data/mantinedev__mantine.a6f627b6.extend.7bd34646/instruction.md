# Bug Report

### Describe the bug

The `extend` method on theme components is broken and causes a syntax error. When trying to use component theme extension, the application fails to compile.

### Reproduction

```tsx
import { Button } from '@mantine/core';

const CustomButton = Button.extend({
  defaultProps: {
    size: 'lg'
  }
});

// Application fails to compile
```

### Expected behavior

The `extend` method should accept an input configuration object and return a properly extended `MantineThemeComponent`. The code should compile and the component should be usable with the extended configuration.

### System Info
- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
