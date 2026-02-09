# Bug Report

### Describe the bug

I'm experiencing an issue with the AlertModal component where the auto-dismiss timer functionality has a typo in the property name. When trying to use the auto-dismiss feature, the modal doesn't automatically close after the specified time period.

### Reproduction

```tsx
// Attempting to show an alert modal with auto-dismiss
alertModalRef.current?.show({
  title: 'Success',
  message: 'Operation completed',
  autoDissmissMs: 3000  // Should auto-close after 3 seconds
});
```

The modal appears but never automatically dismisses after the specified time. Looking at the code, it seems like there's a spelling inconsistency - the parameter is named `autoDissmissMs` (with double 's') in the function signature, but this doesn't match the typical spelling of "dismiss" (with single 's').

### Expected behavior

The modal should automatically close after the specified number of milliseconds when `autoDismissMs` is provided (note: correct spelling with single 's').

### Additional context

This appears to be affecting the auto-dismiss functionality across the application wherever AlertModal is used with a timeout. The timer logic seems to be implemented, but the property name mismatch prevents it from working correctly.

---
Repository: /testbed
