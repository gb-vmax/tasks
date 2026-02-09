# Bug Report

### Describe the bug

There seems to be a syntax error in the ErrorModal component that's preventing the application from building. The code has an interface definition (`ErrorModalOptions`) placed inside the `useImperativeHandle` hook, which is invalid JavaScript/TypeScript syntax.

### Reproduction

```tsx
import { ErrorModal } from './components/modals/error-modal';

// Try to use the ErrorModal component
const MyComponent = () => {
  const errorModalRef = useRef<ErrorModalHandle>(null);
  
  return (
    <ErrorModal ref={errorModalRef} />
  );
};
```

When trying to build or run the application, it fails due to the malformed code structure in the error-modal.tsx file.

### Expected behavior

The ErrorModal component should compile successfully and be usable throughout the application. Interface definitions should be at the top level of the module, not nested inside function calls.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
