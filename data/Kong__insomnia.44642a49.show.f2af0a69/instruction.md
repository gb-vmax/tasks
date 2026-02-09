# Bug Report

### Describe the bug

There's a syntax error in the alert modal component that's breaking the build. The `AlertModalHandle` interface definition appears to be malformed - it looks like implementation code got mixed into the interface declaration.

### Reproduction

When trying to use or import the alert modal component:

```tsx
import { AlertModalHandle } from './components/modals/alert-modal';

// Build fails with syntax errors
```

The interface definition seems to have been corrupted with hook calls and function implementations that shouldn't be there.

### Expected behavior

The `AlertModalHandle` interface should be a clean type definition with just the method signatures:
- `show: (options: AlertModalOptions) => void;`
- `hide: () => void;`

Instead, it appears to contain React hook calls (`useRef`, `useState`, `useImperativeHandle`) and full function implementations which should be in the component body, not in the interface declaration.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is preventing the component from compiling and breaking any imports that reference this modal.

---
Repository: /testbed
