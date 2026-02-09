# Bug Report

### Describe the bug

The ErrorModal component is throwing a syntax error and won't render. After a recent update, the modal completely breaks the application when trying to display error messages.

### Reproduction

```js
import { ErrorModal } from './components/modals/error-modal';

// Try to show an error modal
const errorModalRef = useRef();

// This causes the app to crash
errorModalRef.current?.show({
  title: 'Error',
  message: 'Something went wrong'
});
```

### Expected behavior

The error modal should display properly with the provided title and message. The modal should be able to show and hide without breaking the application.

### System Info
- Insomnia version: latest
- OS: macOS

The application was working fine before the recent changes to the error modal component. Now it seems like there's a structural issue preventing the modal from initializing correctly.

---
Repository: /testbed
