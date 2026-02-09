# Bug Report

### Describe the bug
After a recent update, the `WrapperModal` component seems to have a syntax/structural issue. The modal functionality appears broken - when trying to use the modal in the application, it doesn't work as expected and the component seems to be improperly configured.

### Reproduction
```js
// Try to use WrapperModal in any component
const modalRef = useRef();

// Attempt to show the modal
modalRef.current?.show({ 
  title: 'Test Modal',
  body: <div>Content</div>
});

// Modal doesn't appear or behaves unexpectedly
```

### Expected behavior
The modal should display correctly when `show()` is called. The component structure should be valid and functional.

### System Info
- Insomnia version: Latest
- OS: macOS

### Additional context
This seems to have started happening after some recent changes to the wrapper-modal.tsx file. The modal handle implementation might have some structural issues that are preventing it from working properly.

---
Repository: /testbed
