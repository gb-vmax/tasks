# Bug Report

### Describe the bug

After calling `hide()` on the SelectModal, the modal state is being cleared before the hide animation completes, causing visual glitches. Additionally, the `onCancel` callback is being invoked when explicitly hiding the modal, which is unexpected behavior.

### Reproduction

```js
const modalRef = useRef();

// Show the modal with options
modalRef.current.show({
  title: 'Select an option',
  options: ['Option 1', 'Option 2'],
  onCancel: () => console.log('Cancelled'),
  value: 'Option 1'
});

// Later, explicitly hide the modal
modalRef.current.hide();
// Expected: Modal hides gracefully without triggering onCancel
// Actual: onCancel is called and state is cleared immediately
```

### Expected behavior

When `hide()` is called programmatically:
1. The modal should hide smoothly without clearing state prematurely
2. The `onCancel` callback should NOT be triggered (it should only fire when the user cancels)
3. State cleanup should happen after the modal is fully hidden

### Additional context

This seems to be affecting the modal's ability to maintain its visual state during the hide animation. The `onCancel` callback being fired on programmatic hide is also problematic because it makes it impossible to distinguish between user-initiated cancellation and programmatic dismissal.

---
Repository: /testbed
