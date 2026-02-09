# Bug Report

### Describe the bug
The AlertModal component is broken after a recent change. When trying to use the modal, I'm getting a syntax error and the application fails to compile. It looks like there's a malformed interface definition in the `alert-modal.tsx` file.

### Reproduction
1. Import and try to use the AlertModal component
2. The TypeScript compiler throws an error about the AlertModalHandle interface
3. Application won't build

```tsx
import { AlertModal } from './components/modals/alert-modal';

// This fails to compile
const alertRef = useRef<AlertModalHandle>(null);
```

### Expected behavior
The AlertModalHandle interface should properly define the `show` and `hide` methods as it did before, and the component should compile without errors.

### System Info
- Insomnia version: latest
- Node version: 18.x
- TypeScript version: 5.x

The interface definition seems to have implementation code mixed in where only type definitions should be. This is preventing the entire modal system from working.

---
Repository: /testbed
