# Bug Report

### Describe the bug
The PromptModal component appears to be broken after a recent change. When trying to use the modal, I'm getting TypeScript errors about the interface definition being malformed. The `PromptModalHandle` interface seems to have been corrupted with what looks like implementation code mixed into the interface declaration.

### Reproduction
```tsx
import { PromptModal } from './prompt-modal';

// TypeScript errors when trying to use the modal ref
const modalRef = useRef<PromptModalHandle>(null);

// Attempting to call show() or hide() methods fails
modalRef.current?.show({
  title: 'Enter value',
  defaultValue: '',
  submitName: 'Submit'
});
```

### Expected behavior
The `PromptModalHandle` interface should only contain the method signatures for `show` and `hide`, not the actual component implementation. The modal should be usable with proper TypeScript typing.

### System Info
- Insomnia version: latest
- TypeScript version: 5.x

This is blocking our ability to use any prompt modals in the application. It looks like the interface definition got accidentally replaced with component code.

---
Repository: /testbed
