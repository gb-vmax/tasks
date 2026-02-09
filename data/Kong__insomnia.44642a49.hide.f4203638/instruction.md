# Bug Report

### Describe the bug

After a recent update, there's a syntax error in the `WrapperModal` component that breaks the application. The modal component fails to render and causes the entire UI to crash.

### Reproduction

```tsx
import { WrapperModal } from './components/modals/wrapper-modal';

// Try to use the WrapperModal component
const MyComponent = () => {
  const modalRef = useRef<WrapperModalHandle>(null);
  
  return (
    <WrapperModal ref={modalRef}>
      {/* Modal content */}
    </WrapperModal>
  );
};
```

When attempting to use the WrapperModal component, the application fails to compile/run.

### Expected behavior

The WrapperModal component should work as before, allowing modals to be shown and hidden without compilation errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

The issue appears to be related to the recent changes in the wrapper-modal.tsx file. The component was working fine in the previous version.

---
Repository: /testbed
