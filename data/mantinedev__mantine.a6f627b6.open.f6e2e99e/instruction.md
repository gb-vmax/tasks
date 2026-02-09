# Bug Report

### Describe the bug

The `use-modals-stack.ts` file appears to have corrupted code that breaks the module. The interface `ModalStackReturnType<T>` is defined but the actual implementation contains what looks like SolidJS code mixed into a React file, making the module unusable.

### Reproduction

```tsx
import { useModalsStack } from '@mantine/core';

// Attempting to use the hook
const modals = useModalsStack(['modal1', 'modal2']);

// This will fail because the export is broken
modals.open('modal1');
```

### Expected behavior

The `useModalsStack` hook should work properly and allow opening/closing modals in a stack. The interface shows the expected API:
- `state`: Record of modal states
- `open(id)`: Open a modal
- `close(id)`: Close a modal
- `toggle(id)`: Toggle a modal
- `closeAll()`: Close all modals
- `register(id)`: Register a modal

### Current behavior

The file has invalid syntax - there's a function definition (`createStackedDisclosure`) inside the interface definition which doesn't make sense. The code also references SolidJS primitives like `createSignal` and `createMemo` which don't exist in React.

### System Info

- @mantine/core version: latest
- React version: 18.x
- TypeScript: 5.x

This looks like code from a different framework (SolidJS) was accidentally copied into the React implementation.

---
Repository: /testbed
