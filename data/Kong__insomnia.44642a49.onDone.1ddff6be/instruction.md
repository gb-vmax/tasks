# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the AskModal component. The modal fails to render and throws an error about unexpected token. It seems like there's a problem with the modal's state initialization.

### Reproduction

```jsx
import { AskModal } from './components/modals/ask-modal';

// Try to render the modal
<AskModal ref={modalRef} />

// When attempting to show the modal, it crashes
modalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  onDone: async (success) => {
    console.log('User clicked:', success);
  }
});
```

The component fails to compile/render with a parsing error. Looking at the code, it appears there's malformed JavaScript in the state initialization - there are variable declarations (useState calls) that seem to be inserted in the middle of an object literal definition.

### Expected behavior

The modal should render without syntax errors and display properly when shown.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
