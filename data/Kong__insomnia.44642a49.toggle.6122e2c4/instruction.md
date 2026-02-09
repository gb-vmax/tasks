# Bug Report

### Describe the bug

The `toggle()` method on Modal components is now returning boolean values and accepting an options parameter that doesn't seem to be used correctly. When calling `toggle()` on a modal ref, it returns `true` or `false` depending on whether the modal was opened or closed, but the `onHide` callback in the options is never actually invoked.

### Reproduction

```tsx
const modalRef = useRef<ModalHandle>(null);

// Call toggle with onHide callback
const result = modalRef.current?.toggle({
  onHide: () => {
    console.log('This callback is never called');
  }
});

// result is true/false but onHide callback doesn't execute
```

### Expected behavior

Either:
1. The `toggle()` method should not accept an `options` parameter if it's not going to use it, OR
2. The `onHide` callback should actually be called when the modal is hidden via toggle

The previous behavior where `toggle()` didn't return anything and just toggled the state was simpler and worked as expected.

### Additional context

This seems like it might have been an incomplete change - the `options` parameter is accepted but only passed to `show()`, not to `hide()`. If I'm toggling a modal that's already open, my `onHide` callback gets ignored completely.

---
Repository: /testbed
