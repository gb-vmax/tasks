# Bug Report

### Describe the bug

The `AskModal` component has a syntax error that prevents the application from compiling. When trying to use the modal, the code fails to parse due to incorrect placement of code outside the function scope.

### Reproduction

```js
import { AskModal } from './components/modals/ask-modal';

// Try to render the component
<AskModal ref={modalRef} />
```

The application fails to compile with a syntax error in the `useImperativeHandle` hook implementation.

### Expected behavior

The modal should render and work correctly without compilation errors. The `hide()` and `show()` methods should be properly defined within the imperative handle.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
