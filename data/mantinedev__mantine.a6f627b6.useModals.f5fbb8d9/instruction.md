# Bug Report

### Describe the bug

The `useModals()` hook is returning `undefined` when used inside a `ModalsProvider` context. This breaks all modal functionality as the hook should return the context object with methods like `openModal`, `closeModal`, etc.

### Reproduction

```tsx
import { ModalsProvider, useModals } from '@mantine/modals';

function MyComponent() {
  const modals = useModals();
  
  console.log(modals); // prints undefined instead of context object
  
  // This throws an error because modals is undefined
  const handleClick = () => {
    modals.openModal({
      title: 'Test',
      children: <div>Content</div>
    });
  };
  
  return <button onClick={handleClick}>Open Modal</button>;
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

When `useModals()` is called within a `ModalsProvider`, it should return the context object with all the modal methods. Currently it's returning `undefined` which makes it impossible to use any modal functionality.

The hook should only throw an error when called **outside** of the provider context, not when properly wrapped.

### System Info
- @mantine/modals: latest
- @mantine/core: latest  
- React: 18.x

---
Repository: /testbed
