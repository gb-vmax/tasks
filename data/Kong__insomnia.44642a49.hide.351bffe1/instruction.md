# Bug Report

### Describe the bug

After a recent update, the PromptModal component appears to have a syntax error that prevents the application from compiling. The modal's hide method seems to be malformed - there's code that looks like it belongs inside a function but is placed outside of the method definition.

### Reproduction

```jsx
import { PromptModal } from './components/modals/prompt-modal';

// Try to use the PromptModal component
const modalRef = useRef<PromptModalHandle>(null);

// Attempt to show and hide the modal
modalRef.current?.show({
  title: 'Test Modal',
  defaultValue: 'test'
});

modalRef.current?.hide();
```

The application fails to compile when trying to import or use the PromptModal component.

### Expected behavior

The PromptModal should compile successfully and the hide() method should work as expected without syntax errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
