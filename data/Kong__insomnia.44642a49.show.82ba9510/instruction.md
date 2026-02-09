# Bug Report

### Describe the bug

The AlertModal component is broken after a recent update. When trying to use the modal, I'm getting TypeScript errors and the component doesn't render at all. It looks like there's a syntax issue with the interface definition.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

const MyComponent = () => {
  const alertModalRef = useRef<AlertModalHandle>(null);
  
  const handleClick = () => {
    alertModalRef.current?.show({
      title: 'Test Alert',
      message: 'This is a test message'
    });
  };
  
  return (
    <>
      <button onClick={handleClick}>Show Alert</button>
      <AlertModal ref={alertModalRef} />
    </>
  );
};
```

When trying to compile or use this component, it fails because the `AlertModalHandle` interface is malformed.

### Expected behavior

The AlertModal should render and show alerts when the `show` method is called on the ref. The TypeScript interface should be properly defined with the `show` and `hide` methods.

### System Info
- Insomnia version: latest
- TypeScript version: 4.x

The interface definition seems to have code mixed into it where there should only be type definitions. This is preventing the component from being used at all.

---
Repository: /testbed
