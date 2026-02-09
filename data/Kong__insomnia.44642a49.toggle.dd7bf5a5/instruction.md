# Bug Report

### Describe the bug

The `toggle()` method on Modal components doesn't accept options when toggling from closed to open state. When calling `toggle()` with options parameter, the options are ignored and the modal opens without applying them.

### Reproduction

```js
const modalRef = useRef();

// Later in code:
// Trying to toggle modal with options
modalRef.current.toggle({ onClose: handleClose });

// The modal opens but the options are not applied
// Expected: modal should open with onClose callback
// Actual: modal opens without the callback
```

The issue is that `toggle()` internally calls `show()` but doesn't forward any options to it. If you call `show(options)` directly it works fine, but using `toggle(options)` loses the options.

### Expected behavior

When calling `toggle(options)` on a closed modal, it should pass the options to the `show()` method so that the modal opens with the specified configuration (callbacks, etc.).

### Workaround

Currently have to check the state manually and call `show()` or `hide()` directly:
```js
if (modalRef.current.isOpen()) {
  modalRef.current.hide();
} else {
  modalRef.current.show(options);
}
```

---
Repository: /testbed
