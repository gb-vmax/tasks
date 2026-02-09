# Bug Report

### Describe the bug

The `useModals` hook is throwing an error even when used inside a `ModalsProvider` component. The error message says "useModals hook was called outside of context" but the hook is definitely being called within the provider.

### Reproduction

```jsx
import { ModalsProvider, useModals } from '@mantine/modals';

function MyComponent() {
  const modals = useModals(); // This throws an error
  
  return <div>Component content</div>;
}

function App() {
  return (
    <ModalsProvider>
      <MyComponent />
    </ModalsProvider>
  );
}
```

### Expected behavior

The hook should return the modals context object when called inside `ModalsProvider` and only throw an error when called outside of it.

### System Info

- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
