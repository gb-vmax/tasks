# Bug Report

### Describe the bug

The `toggle()` method on Modal components is not calling the `onToggle` callback when toggling the modal state. I'm trying to track when a modal opens/closes using the callback, but it never gets invoked.

### Reproduction

```js
const modalRef = useRef();

// Try to toggle with callback
modalRef.current?.toggle({
  onToggle: (newState) => {
    console.log('Modal toggled to:', newState);
  }
});

// The console.log never fires
```

### Expected behavior

When calling `toggle()` with an `onToggle` callback, the callback should be invoked with the new state (true for open, false for closed) after the toggle operation completes.

### Additional context

This seems to affect any code that needs to react to modal state changes when using the toggle method. The `show()` and `hide()` methods work fine, but `toggle()` doesn't provide a way to know what the new state is without manually tracking it externally.

---
Repository: /testbed
