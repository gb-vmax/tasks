# Bug Report

### Describe the bug

The `useModals` hook is throwing an error even when used inside a `ModalsProvider` component. The error message says the hook was called outside of context, but I've confirmed that my component is properly wrapped with `ModalsProvider`.

### Reproduction

```jsx
import { ModalsProvider, useModals } from '@mantine/modals';

function MyComponent() {
  const modals = useModals(); // This throws an error
  
  return <div>Content</div>;
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

The hook should return the modals context without throwing an error when used inside `ModalsProvider`. Instead, it's throwing:

```
[@mantine/modals] useModals hook was called outside of context, wrap your app with ModalsProvider component
```

This is really confusing because the component IS wrapped with `ModalsProvider`. The hook seems to be checking for the context incorrectly.

### System Info
- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
