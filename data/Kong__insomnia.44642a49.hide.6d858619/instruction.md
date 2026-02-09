# Bug Report

### Describe the bug

I'm experiencing an issue with the AlertModal component where the interface definition `AlertModalOptions` is appearing in the middle of the `useImperativeHandle` hook instead of being at the top level. This causes a syntax error and breaks the component completely.

### Reproduction

```tsx
import { AlertModal } from './components/modals/alert-modal';

// Try to use the AlertModal component
const modalRef = useRef<AlertModalHandle>(null);

// This will fail to compile/run due to malformed code
<AlertModal ref={modalRef} />
```

The code structure is broken - there's a TypeScript interface definition placed inside the `useImperativeHandle` hook which is invalid syntax.

### Expected behavior

The `AlertModalOptions` interface should be defined at the module level (outside of the component), and the `useImperativeHandle` hook should only contain the implementation of the handle methods (`hide` and `show`).

The component should compile and function correctly.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
