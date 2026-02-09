# Bug Report

### Describe the bug

The AskModal component seems to have broken syntax after a recent change. When trying to use the modal, the application fails to compile/run due to what appears to be malformed code in the modal's implementation.

### Reproduction

```jsx
import { AskModal } from './components/modals/ask-modal';

// Try to render or use the AskModal component
const modalRef = useRef();

// Attempting to show the modal
modalRef.current?.show({
  title: 'Confirm Action',
  message: 'Are you sure?',
  onDone: (result) => console.log(result)
});
```

### Expected behavior

The modal should render and function normally without any compilation or runtime errors. The `hide()` and `show()` methods should be properly defined and accessible through the ref.

### Additional context

This appears to have started happening recently. The modal component seems to have some structural issues in its implementation that prevent it from working at all. Looking at the code, it seems like there might be some misplaced hooks or improperly nested function definitions.

---
Repository: /testbed
