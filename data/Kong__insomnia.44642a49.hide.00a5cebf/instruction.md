# Bug Report

### Describe the bug

The AlertModal component is not properly structured - there's an interface definition (`AlertModalOptions`) that appears to be placed inside the `useImperativeHandle` hook instead of at the top level of the file. This causes a syntax error and prevents the component from rendering.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal component
const MyComponent = () => {
  const alertRef = useRef<AlertModalHandle>(null);
  
  const handleClick = () => {
    alertRef.current?.show({
      title: 'Test Alert',
      message: 'This is a test message'
    });
  };
  
  return (
    <>
      <button onClick={handleClick}>Show Alert</button>
      <AlertModal ref={alertRef} />
    </>
  );
};
```

When trying to use the component, the application fails to compile due to the malformed code structure.

### Expected behavior

The `AlertModalOptions` interface should be defined at the module level (outside the component), and the `hide` method should be properly defined within the `useImperativeHandle` hook without any interface definitions mixed in.

### System Info
- Insomnia packages version: latest
- Node version: 18.x

---
Repository: /testbed
