# Bug Report

### Describe the bug

After a recent update, the `DirectionProvider` is throwing errors when trying to toggle direction. The `toggleDirection` function seems to be referencing properties that don't exist on the context object (`this.direction`, `this.reversed`, `this.onDirectionChange`).

### Reproduction

```jsx
import { DirectionProvider, useDirection } from '@mantine/core';

function MyComponent() {
  const { toggleDirection } = useDirection();
  
  return (
    <button onClick={toggleDirection}>
      Toggle Direction
    </button>
  );
}

function App() {
  return (
    <DirectionProvider>
      <MyComponent />
    </DirectionProvider>
  );
}
```

When clicking the button, I get errors about undefined properties being accessed.

### Expected behavior

The `toggleDirection` function should work without errors and toggle between 'ltr' and 'rtl' directions as it did before.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
