# Bug Report

### Describe the bug

After a recent update, the `extend` method on theme components appears to be broken. When trying to extend a component's theme configuration, I'm getting a syntax error that prevents the application from compiling.

### Reproduction

```tsx
import { factory } from '@mantine/core';

const MyComponent = factory((props, ref) => {
  return <div ref={ref} {...props} />;
});

// Trying to extend the component theme
const theme = createTheme({
  components: {
    MyComponent: MyComponent.extend({
      defaultProps: {
        size: 'md',
      },
      classNames: {
        root: 'custom-class',
      },
    }),
  },
});
```

### Expected behavior

The component should extend properly and the theme configuration should be applied without any compilation errors. The `extend` method should merge the base component's theme properties with the extended properties.

### System Info

- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

The code doesn't compile at all, so I can't even test if the functionality works. It looks like there might be a syntax issue in the factory implementation itself.

---
Repository: /testbed
