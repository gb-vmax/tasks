# Bug Report

### Describe the bug

After a recent update, the AlertModal component is completely broken. When trying to use the modal in the application, I'm getting TypeScript errors and the modal doesn't render at all.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Trying to use the AlertModal component
const modalRef = useRef<AlertModalHandle>(null);

// Later in code:
modalRef.current?.show({
  title: 'Warning',
  message: 'Are you sure?',
  onConfirm: () => console.log('confirmed')
});
```

This code now fails with TypeScript compilation errors. The `AlertModalHandle` interface seems to have been corrupted or malformed.

### Expected behavior

The AlertModal should work as before - the `show()` and `hide()` methods should be available on the handle interface and the modal should display properly when called.

### System Info
- Insomnia version: latest
- OS: macOS

The interface definition looks completely wrong now. It seems like some code got accidentally merged into the interface definition instead of being in the right place.

---
Repository: /testbed
