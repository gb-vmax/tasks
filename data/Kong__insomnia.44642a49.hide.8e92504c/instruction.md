# Bug Report

### Describe the bug
The ErrorModal component is throwing a syntax error and failing to render. It seems like there's an issue with the `useImperativeHandle` implementation where the code structure is malformed.

### Reproduction
```tsx
import { ErrorModal } from './components/modals/error-modal';

// Try to use the ErrorModal component
const modalRef = useRef<ErrorModalHandle>(null);

// Component fails to render with syntax error
<ErrorModal ref={modalRef} />
```

When trying to use the ErrorModal component, the application crashes immediately with a parsing error. The modal cannot be instantiated or shown.

### Expected behavior
The ErrorModal should render without errors and the `hide()` method should work correctly when called via the ref.

### System Info
- Insomnia version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
