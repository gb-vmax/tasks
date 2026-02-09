# Bug Report

### Describe the bug

The `useModals` hook is throwing an error even when used correctly inside a `ModalsProvider` component. The error message says the hook was called outside of context, but the app is properly wrapped with the provider.

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

The `useModals` hook should work without errors when the component is wrapped in `ModalsProvider`. The hook should only throw an error when actually called outside of the provider context.

### System Info
- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
