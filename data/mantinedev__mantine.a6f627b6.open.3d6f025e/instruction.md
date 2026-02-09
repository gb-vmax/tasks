# Bug Report

### Describe the bug

I'm experiencing an issue with the modals stack manager where closing a modal doesn't work correctly. When I try to close a modal that's currently open, it doesn't actually close - the modal remains visible and the stack state seems corrupted.

### Reproduction

```jsx
const { state, open, close, register } = useModalsStack(['modal1', 'modal2', 'modal3']);

// Open multiple modals
open('modal1');
open('modal2');
open('modal3');

// Try to close modal2 (middle modal)
close('modal2');

// Expected: modal2 should be closed
// Actual: modal2 remains open, or wrong modal gets closed
```

### Expected behavior

When calling `close(id)` on a modal, that specific modal should be removed from the stack and closed. The other modals should remain unaffected.

Currently it seems like the close logic is filtering incorrectly - sometimes it keeps the last modal open even when trying to close it, or removes the wrong modal from the stack entirely.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
