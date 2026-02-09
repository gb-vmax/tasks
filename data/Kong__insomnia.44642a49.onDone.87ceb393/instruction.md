# Bug Report

### Describe the bug

The AskModal component appears to have a syntax error that's preventing the application from compiling. There seems to be an issue with the state initialization where interface definitions and function declarations are mixed together incorrectly.

### Reproduction

When trying to use the AskModal component:

```tsx
import { AskModal } from './components/modals/ask-modal';

// Component fails to render
<AskModal ref={modalRef} />
```

The application fails to compile with a syntax error related to the modal's state initialization.

### Expected behavior

The AskModal should initialize properly with its default state values and render without compilation errors. The modal should be able to accept options like `title`, `message`, `yesText`, `noText`, and `color` as before.

### System Info
- Insomnia version: Latest
- Node version: 18.x

This seems to have started happening recently. The modal was working fine before but now the entire component appears to be broken due to malformed code structure.

---
Repository: /testbed
