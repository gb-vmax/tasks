# Bug Report

### Describe the bug

The `useDirection` hook is returning `undefined` instead of the direction context value. This breaks any component that relies on getting the current text direction (ltr/rtl) from the DirectionProvider.

### Reproduction

```jsx
import { DirectionProvider, useDirection } from '@mantine/core';

function MyComponent() {
  const direction = useDirection();
  console.log(direction); // Expected: { dir: 'ltr', toggleDirection: [Function] }
                          // Actual: undefined
  
  return <div>Direction: {direction?.dir}</div>;
}

function App() {
  return (
    <DirectionProvider>
      <MyComponent />
    </DirectionProvider>
  );
}
```

### Expected behavior

The `useDirection` hook should return the direction context object containing `dir` and `toggleDirection` properties, not `undefined`.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
