# Bug Report

### Describe the bug

The spotlight component fails to open when calling the `open()` action. After calling `spotlight.open()`, nothing happens and the spotlight doesn't appear on the screen.

### Reproduction

```js
import { createSpotlight } from '@mantine/spotlight';

const spotlight = createSpotlight();

// Try to open the spotlight
spotlight.open();

// Expected: Spotlight opens
// Actual: Nothing happens, spotlight doesn't open
```

### Expected behavior

When calling `spotlight.open()`, the spotlight component should open and be visible on the screen.

### System Info

- @mantine/spotlight version: latest
- Browser: Chrome

---
Repository: /testbed
