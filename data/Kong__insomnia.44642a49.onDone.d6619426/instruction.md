# Bug Report

### Describe the bug

The AskModal component is broken after a recent change. The modal doesn't render properly and the application crashes when trying to display it.

### Reproduction

1. Trigger any action that uses the AskModal component
2. The modal fails to render and shows a blank screen or error

Example code that would trigger the modal:
```js
const askModal = useRef();

// Later in the code
askModal.current?.show({
  title: 'Delete Item',
  message: 'Are you sure you want to delete this item?',
  yesText: 'Delete',
  noText: 'Cancel',
  onDone: async (success) => {
    if (success) {
      await deleteItem();
    }
  }
});
```

### Expected behavior

The modal should display with the title, message, and action buttons (Yes/No). Clicking either button should execute the callback and close the modal.

### System Info
- Insomnia version: latest
- OS: macOS

The modal was working fine before, but something in the recent changes seems to have broken the component structure. The code appears to have incomplete or malformed JSX/TypeScript.

---
Repository: /testbed
