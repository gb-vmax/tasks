# Bug Report

### Describe the bug

The `AlertModal` component has a structural issue where helper functions (`clearAutoDismiss` and `scheduleAutoDismiss`) are being defined inside the `useImperativeHandle` hook, which breaks the component's functionality. The code structure is invalid and will cause the modal to not work correctly.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal with the show method
const modalRef = useRef<AlertModalHandle>(null);

// This will fail because the internal structure is broken
modalRef.current?.show({
  title: 'Test Alert',
  message: 'This is a test message',
  onConfirm: () => console.log('Confirmed')
});
```

### Expected behavior

The modal should display properly when `show()` is called. The helper functions should be defined outside of the `useImperativeHandle` hook so that the `hide` and `show` methods are properly structured and accessible.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
