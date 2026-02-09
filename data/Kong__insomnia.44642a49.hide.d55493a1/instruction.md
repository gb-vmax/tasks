# Bug Report

### Describe the bug

After a recent update, the `WrapperModal` component seems to have broken functionality. When trying to use the modal, I'm getting errors and the modal doesn't work properly anymore.

### Reproduction

```tsx
import { WrapperModal } from './components/modals/wrapper-modal';

const modalRef = useRef<WrapperModalHandle>(null);

// Try to show the modal
modalRef.current?.show({
  title: 'Test Modal',
  body: <div>Modal content</div>
});

// Later try to hide it
modalRef.current?.hide();
```

### Expected behavior

The modal should show and hide without any errors. The `show` and `hide` methods should work as they did before.

### Additional context

This appears to be a syntax/structural issue in the component code itself. The modal component was working fine previously but now throws errors when trying to use it. Looking at the code, there seems to be some malformed structure in the `useImperativeHandle` implementation.

---
Repository: /testbed
