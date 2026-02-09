# Bug Report

### Describe the bug

When trying to extend a Mantine component using the theme's `extend` method, I'm getting a syntax error. It seems like the `extend` function definition is broken in the latest version.

### Reproduction

```tsx
import { createTheme } from '@mantine/core';

const theme = createTheme({
  components: {
    Button: Button.extend({
      defaultProps: {
        size: 'md',
      },
    }),
  },
});
```

When I try to use this code, TypeScript throws an error and the application fails to compile. The `extend` method doesn't seem to be properly defined.

### Expected behavior

The `extend` method should accept an `ExtendComponent` input and return a `MantineThemeComponent` that can be used to customize component behavior.

### System Info

- @mantine/core version: latest
- TypeScript version: 5.x
- React version: 18.x

This was working fine in the previous version, but after updating I started seeing this issue. It looks like there might be a syntax problem with how the `extend` method is defined in the factory types.

---
Repository: /testbed
