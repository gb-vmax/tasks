# Bug Report

### Describe the bug

The AlertModal component is broken after a recent change. When trying to use the modal, I'm getting a syntax error and the application fails to compile. It looks like the interface definition for `AlertModalHandle` was accidentally replaced with implementation code.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal component
const MyComponent = () => {
  const alertModalRef = useRef<AlertModalHandle>(null);
  
  const showAlert = () => {
    alertModalRef.current?.show({
      title: 'Test Alert',
      message: 'This is a test message'
    });
  };
  
  return (
    <>
      <button onClick={showAlert}>Show Alert</button>
      <AlertModal ref={alertModalRef} />
    </>
  );
};
```

### Expected behavior

The AlertModal component should compile and work normally. The `AlertModalHandle` interface should define the `show` and `hide` methods that can be called via ref.

### Actual behavior

The application fails to compile with syntax errors. The interface definition appears to have been corrupted with React hooks and implementation logic that doesn't belong there.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
