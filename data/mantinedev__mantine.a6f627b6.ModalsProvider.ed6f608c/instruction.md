# Bug Report

### Describe the bug

The `closeAll` method in ModalsProvider is not respecting the `canceled` parameter. When calling `modals.closeAll(true)` to close all modals with a canceled state, the parameter is being ignored and all modals are closed with `canceled: false` instead.

### Reproduction

```tsx
import { modals } from '@mantine/modals';

// Open a modal with onCancel callback
modals.open({
  modalId: 'test-modal',
  title: 'Test',
  children: <div>Content</div>,
  onCancel: () => console.log('Modal was canceled'),
});

// Try to close all modals as canceled
modals.closeAll(true);

// Expected: onCancel callback should be triggered
// Actual: onCancel callback is not triggered because canceled=false is hardcoded
```

### Expected behavior

When calling `modals.closeAll(true)`, the `canceled` parameter should be passed through to the dispatch action so that modal callbacks can properly distinguish between canceled and non-canceled closures.

### System Info
- @mantine/modals version: latest
- React version: 18.x

---
Repository: /testbed
