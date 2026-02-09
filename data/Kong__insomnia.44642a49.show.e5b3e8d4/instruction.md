# Bug Report

### Describe the bug

The PromptModal component is broken after a recent change. The modal interface definition appears to be corrupted - instead of properly defining the `show` and `hide` methods, there's implementation code mixed into the interface declaration itself.

### Reproduction

When trying to use the PromptModal component:

```tsx
import { PromptModal } from './components/modals/prompt-modal';

const MyComponent = () => {
  const promptModalRef = useRef<PromptModalHandle>(null);
  
  const handleClick = () => {
    // This will fail because the interface is malformed
    promptModalRef.current?.show({
      title: 'Enter value',
      defaultValue: '',
      onComplete: (value) => {
        console.log(value);
      }
    });
  };
  
  return (
    <>
      <button onClick={handleClick}>Show Prompt</button>
      <PromptModal ref={promptModalRef} />
    </>
  );
};
```

### Expected behavior

The PromptModalHandle interface should properly define the type signatures for `show` and `hide` methods without including implementation details. The modal should be able to be shown and hidden normally.

### System Info

- Insomnia version: latest
- The issue appears in `packages/insomnia/src/ui/components/modals/prompt-modal.tsx`

This looks like implementation code accidentally got placed inside the interface definition block instead of in the component body. The interface should only contain type definitions, not actual function implementations.

---
Repository: /testbed
