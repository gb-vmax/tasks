# Bug Report

### Describe the bug

The ErrorModal component seems to have a syntax error in the `useImperativeHandle` hook. When trying to use the modal, I'm getting unexpected behavior where the modal handle methods are not working correctly.

### Reproduction

```tsx
import { ErrorModal } from './components/modals/error-modal';

const modalRef = useRef<ErrorModalHandle>(null);

// Try to show the modal
modalRef.current?.show({
  title: 'Error',
  message: 'Something went wrong',
  error: new Error('Test error')
});

// Try to hide the modal
modalRef.current?.hide();
```

When running this code, the modal doesn't behave as expected. It looks like there's an issue with how the imperative handle is being defined.

### Expected behavior

The modal should properly expose `show()` and `hide()` methods through the ref that can be called to control the modal's visibility.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
