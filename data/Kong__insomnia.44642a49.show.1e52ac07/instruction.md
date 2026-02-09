# Bug Report

### Describe the bug

After a recent update, the AlertModal component is broken and doesn't work at all. When trying to use the modal, the application crashes or the modal doesn't show up. It looks like there's a syntax error or something wrong with the modal interface definition.

### Reproduction

```js
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal
const modalRef = useRef();

// Attempting to show the modal
modalRef.current.show({
  title: 'Test Alert',
  message: 'This is a test message'
});
```

### Expected behavior

The modal should display with the title and message. Instead, the code doesn't even compile or the modal handle is completely broken.

### Additional context

This seems to have broken after changes to the AlertModalHandle interface. The interface definition looks malformed - it seems like there's code mixed in where only type definitions should be.

---
Repository: /testbed
