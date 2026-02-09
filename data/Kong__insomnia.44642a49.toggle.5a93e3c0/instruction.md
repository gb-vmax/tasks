# Bug Report

### Describe the bug

The `toggle()` method on Modal components is not respecting the current open state correctly. When calling `toggle()` with options, it seems to check the state before the toggle happens rather than after, leading to unexpected behavior where the modal doesn't open with the provided options.

### Reproduction

```tsx
const modalRef = useRef<ModalHandle>(null);

// Try to toggle the modal with options
const handleClick = () => {
  modalRef.current?.toggle({ tall: true });
};

// The modal doesn't receive the options properly
// Expected: modal opens with tall=true
// Actual: options are ignored or applied incorrectly
```

### Steps to reproduce
1. Create a modal with a ref
2. Call `toggle()` with options parameter (e.g., `{ tall: true }`)
3. The modal state changes but the options aren't applied as expected

### Expected behavior

When calling `toggle(options)`, the modal should:
- Toggle its open/closed state
- Apply the provided options when opening
- Work consistently regardless of the current state

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
