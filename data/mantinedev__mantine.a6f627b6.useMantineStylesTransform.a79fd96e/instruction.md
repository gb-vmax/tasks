# Bug Report

### Describe the bug

I'm encountering an issue where `useMantineStylesTransform()` is not returning the correct value. It seems like the function is trying to access a property that doesn't exist, causing my application to break when trying to use styles transform.

### Reproduction

```tsx
import { useMantineStylesTransform } from '@mantine/core';

function MyComponent() {
  const stylesTransform = useMantineStylesTransform();
  
  // This throws an error or returns undefined
  console.log(stylesTransform);
  
  return <div>Test</div>;
}
```

When I try to use `useMantineStylesTransform()` in my component, I'm getting unexpected behavior. The hook doesn't seem to be accessing the right property from the context.

### Expected behavior

The `useMantineStylesTransform()` hook should return the styles transform configuration from the Mantine context properly, allowing me to use it in my components without errors.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
