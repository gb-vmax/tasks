# Bug Report

### Describe the bug

The AskModal component is broken after a recent change. When trying to use the modal, it doesn't render properly and the application crashes. It looks like the refactoring was incomplete or got corrupted somehow.

### Reproduction

```jsx
import { AskModal } from './components/modals/ask-modal';

// Try to use the modal
const modalRef = useRef();

modalRef.current?.show({
  title: 'Delete Item',
  message: 'Are you sure you want to delete this?',
  yesText: 'Delete',
  noText: 'Cancel',
  onDone: async (success) => {
    if (success) {
      // handle deletion
    }
  }
});
```

When this code runs, the modal doesn't appear and there are syntax errors in the console.

### Expected behavior

The modal should display with the title, message, and buttons as configured. The `onDone` callback should be called when a button is clicked.

### Additional context

This was working fine before but seems to have broken recently. The component file looks like it has incomplete code - there's a `<di` tag at the end that doesn't look right. The structure of the component also seems malformed with interfaces and functions defined in weird places.

---
Repository: /testbed
