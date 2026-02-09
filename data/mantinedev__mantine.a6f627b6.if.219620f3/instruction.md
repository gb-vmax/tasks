# Bug Report

### Describe the bug

When passing `null` as a value to components that use responsive props, the application crashes with a runtime error. This seems to be a regression as `null` values were previously handled correctly.

### Reproduction

```tsx
import { Box } from '@mantine/core';

function MyComponent() {
  return (
    <Box p={null}>
      Content
    </Box>
  );
}
```

The component throws an error when trying to read properties of `null`. This affects any component prop that supports responsive values (objects with `base`, `xs`, `sm`, etc.).

### Expected behavior

Passing `null` should be handled gracefully, either by treating it as "no value" or by returning `null` itself. The component should not crash.

### Additional context

This happens with any prop that accepts `StyleProp<T>` types. Examples include padding, margin, width, height, etc.

It looks like the issue is related to how the base value is extracted from responsive prop objects, but `null` is being treated as an object which causes the error.

---
Repository: /testbed
