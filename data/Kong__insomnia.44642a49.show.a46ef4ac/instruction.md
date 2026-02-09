# Bug Report

### Describe the bug

The AlertModal component appears to have duplicate interface definitions and the component implementation is broken. When trying to use the AlertModal, the application fails to compile due to syntax errors in the modal component file.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Attempting to use the AlertModal component
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

The file fails to compile with syntax errors. Looking at the source, the `AlertModalHandle` interface is defined twice, and the component code appears to have incomplete/malformed code at the end of the `onClick` handler.

### Expected behavior

The AlertModal component should compile successfully and be usable for displaying alert dialogs with the specified options (title, message, cancel button, etc.).

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
