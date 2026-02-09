# Bug Report

### Describe the bug

I'm getting a syntax error when trying to use the PromptModal component. The application won't compile and throws an error about unexpected token in the prompt-modal.tsx file.

### Reproduction

```tsx
import { PromptModal } from './components/modals/prompt-modal';

function MyComponent() {
  const promptModalRef = useRef<PromptModalHandle>(null);
  
  const handleClick = () => {
    promptModalRef.current?.show({
      title: 'Enter value',
      defaultValue: '',
      submitName: 'Submit',
      onComplete: (value) => console.log(value)
    });
  };
  
  return (
    <>
      <button onClick={handleClick}>Open Prompt</button>
      <PromptModal ref={promptModalRef} />
    </>
  );
}
```

When I try to build or run the app with this code, I get a compilation error pointing to the PromptModalHandle interface definition in prompt-modal.tsx.

### Expected behavior

The component should compile successfully and the modal should be usable as before.

### System Info
- Insomnia version: Latest
- Node version: 18.x

This seems to have been introduced recently as the code was working fine before. The interface definition appears to be malformed somehow.

---
Repository: /testbed
