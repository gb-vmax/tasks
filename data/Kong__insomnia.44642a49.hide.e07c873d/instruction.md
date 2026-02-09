# Bug Report

### Describe the bug

There's an issue with the AlertModal component where the interface definition `AlertModalOptions` is placed inside the `useImperativeHandle` hook instead of at the top level. This causes a syntax error and prevents the component from rendering properly.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal component
const MyComponent = () => {
  const alertRef = useRef<AlertModalHandle>(null);
  
  const showAlert = () => {
    alertRef.current?.show({
      title: 'Test Alert',
      message: 'This is a test message'
    });
  };
  
  return (
    <>
      <button onClick={showAlert}>Show Alert</button>
      <AlertModal ref={alertRef} />
    </>
  );
};
```

When trying to render a component that uses AlertModal, the app crashes with a syntax error. The modal component fails to compile/load.

### Expected behavior

The AlertModal should render without errors and the interface should be properly defined at the module level, not nested inside the hook implementation.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
