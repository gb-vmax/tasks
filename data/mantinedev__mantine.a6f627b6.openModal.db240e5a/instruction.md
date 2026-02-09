# Bug Report

### Describe the bug

When opening multiple modals in sequence, the second modal gets the wrong settings/configuration from the previous modal. It seems like there's some kind of overwriting happening where the new modal inherits properties from the modal that was opened before it.

### Reproduction

```js
import { modals } from '@mantine/modals';

// Open first modal
const firstModalId = modals.openModal({
  title: 'First Modal',
  content: 'This is the first modal',
  size: 'small'
});

// Open second modal
const secondModalId = modals.openModal({
  title: 'Second Modal',
  content: 'This is the second modal',
  size: 'large'
});

// The second modal displays with settings from the first modal
// Expected: Second modal should have its own title, content, and size
// Actual: Second modal shows "First Modal" title and content
```

### Expected behavior

Each modal should maintain its own independent settings. When opening a second modal while the first is still open, the second modal should display with its own title, content, and size properties, not inherit anything from the first modal.

### System Info
- @mantine/modals version: latest
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
