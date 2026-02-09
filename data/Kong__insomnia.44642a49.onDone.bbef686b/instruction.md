# Bug Report

### Describe the bug

The AskModal component is broken after a recent change. When trying to use the modal, I'm getting a syntax error and the modal doesn't render at all. The application crashes when attempting to show an AskModal.

### Reproduction

```jsx
import { AskModal } from './components/modals/ask-modal';

// Try to use AskModal in a component
const MyComponent = () => {
  const askModalRef = useRef();
  
  const handleClick = () => {
    askModalRef.current?.show({
      title: 'Confirm Action',
      message: 'Are you sure?',
      onDone: async (success) => {
        if (success) {
          // do something
        }
      }
    });
  };
  
  return (
    <>
      <button onClick={handleClick}>Show Modal</button>
      <AskModal ref={askModalRef} />
    </>
  );
};
```

### Expected behavior

The modal should display properly and allow users to confirm or cancel actions. The `onDone` callback should be called when the user clicks Yes or No.

### Actual behavior

The component fails to compile/render. Looking at the code, it seems like there's a syntax issue in the state initialization - there are hooks and handler functions mixed into what looks like it should be a state object definition.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
