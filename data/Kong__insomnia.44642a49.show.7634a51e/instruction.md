# Bug Report

### Describe the bug

The PromptModal component is broken after a recent change. The modal interface definition appears to be corrupted with implementation code mixed into the type definition, causing TypeScript compilation errors and preventing the modal from being used anywhere in the application.

### Reproduction

Try to use the PromptModal component in any part of the codebase:

```tsx
import { PromptModal } from './components/modals/prompt-modal';

// This will fail to compile
const modalRef = useRef<PromptModalHandle>(null);

// Cannot call show() method
modalRef.current?.show({
  title: 'Enter value',
  defaultValue: 'test'
});
```

The TypeScript compiler throws errors because the `PromptModalHandle` interface definition contains implementation code (hooks, functions, JSX) instead of just the method signatures.

### Expected behavior

The `PromptModalHandle` interface should only contain type definitions for the `show` and `hide` methods, not actual implementation code. The modal should be usable throughout the application without compilation errors.

### System Info
- Insomnia version: latest
- The issue appears to be in the prompt-modal.tsx file where the interface definition was accidentally replaced with implementation code

---
Repository: /testbed
