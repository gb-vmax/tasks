# Bug Report

### Describe the bug

The `useDirection()` hook is returning `undefined` when a valid direction context is provided. This breaks any component that relies on reading the current direction (ltr/rtl) from the context.

### Reproduction

```jsx
import { DirectionProvider, useDirection } from '@mantine/core';

function MyComponent() {
  const { dir } = useDirection();
  console.log(dir); // Expected: 'ltr' or 'rtl', Actual: undefined
  
  return <div>Direction: {dir}</div>;
}

function App() {
  return (
    <DirectionProvider dir="rtl">
      <MyComponent />
    </DirectionProvider>
  );
}
```

### Expected behavior

`useDirection()` should return the direction context object with the current `dir` value ('ltr' or 'rtl') when used inside a `DirectionProvider`.

### System Info

- @mantine/core version: latest
- React version: 18.x

This seems to have started happening recently. Components that depend on direction information are now showing undefined instead of the actual direction value.

---
Repository: /testbed
