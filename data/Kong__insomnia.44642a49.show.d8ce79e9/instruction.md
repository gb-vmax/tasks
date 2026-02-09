# Bug Report

### Describe the bug

The `WrapperModal` component has a syntax error that prevents the application from compiling. There appears to be a malformed interface definition that's placed in the middle of the component's imperative handle implementation, breaking the code structure.

### Reproduction

When trying to use the `WrapperModal` component or any component that imports it, the application fails to build with a syntax error. The issue is in the `wrapper-modal.tsx` file where the `show` method is defined.

```tsx
import { WrapperModal } from './components/modals/wrapper-modal';

// Simply trying to import or use this component will cause build failure
const MyComponent = () => {
  const modalRef = useRef<WrapperModalHandle>(null);
  
  return (
    <WrapperModal ref={modalRef} />
  );
};
```

### Expected behavior

The component should compile successfully and be usable without syntax errors. The interface definition should be properly placed outside of the imperative handle implementation.

### System Info

- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
