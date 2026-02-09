# Bug Report

### Describe the bug

The `useModals` hook is throwing an error when called inside a component that's properly wrapped with `ModalsProvider`. The error message says the hook was called outside of context, but that's not the case - the provider is correctly set up in my app.

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

The hook should return the modals context without throwing an error when used inside a component wrapped with `ModalsProvider`.

### Actual behavior

Getting this error:
```
Error: [@mantine/modals] useModals hook was called outside of context, wrap your app with ModalsProvider component
```

Even though the component IS wrapped with the provider.

### System Info
- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
