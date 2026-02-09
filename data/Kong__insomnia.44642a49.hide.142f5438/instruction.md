# Bug Report

### Describe the bug

The `WrapperModal` component crashes when trying to hide the modal. After a recent update, calling the `hide()` method results in a syntax error and the modal cannot be closed properly.

### Reproduction

```tsx
const modalRef = useRef<WrapperModalHandle>(null);

// Show the modal
modalRef.current?.show({
  title: 'Test Modal',
  body: <div>Content</div>
});

// Try to hide the modal - this causes an error
modalRef.current?.hide();
```

### Expected behavior

The modal should close without errors when `hide()` is called. The modal was working fine before but now throws an error immediately when attempting to hide it.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
