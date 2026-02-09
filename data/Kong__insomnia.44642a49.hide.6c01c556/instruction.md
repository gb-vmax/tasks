# Bug Report

### Describe the bug

The SelectModal component is calling `onCancel` callback when the modal is hidden, even when it's been explicitly dismissed through a selection or other completion action. This causes the cancel handler to fire inappropriately in scenarios where the user has already completed an action.

### Reproduction

```js
const handleCancel = () => {
  console.log('User cancelled');
};

const handleSelect = (item) => {
  console.log('User selected:', item);
  selectModalRef.current?.hide();
};

// Show modal with cancel handler
selectModalRef.current?.show({
  items: [...],
  onSelect: handleSelect,
  onCancel: handleCancel
});

// When user selects an item:
// 1. handleSelect is called correctly
// 2. hide() is called to close the modal
// 3. handleCancel is ALSO called (unexpected!)
```

### Expected behavior

The `onCancel` callback should only be triggered when the user actually cancels the modal (e.g., clicking outside, pressing ESC, clicking a cancel button), not when the modal is programmatically hidden after a successful action.

In the example above, only `handleSelect` should be called when the user makes a selection. The `handleCancel` callback should not fire.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
