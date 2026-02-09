# Bug Report

### Describe the bug

When calling `spotlight.close()` multiple times or in certain conditions, the spotlight modal closes twice instead of once. This causes unexpected behavior where the close action is triggered redundantly.

### Reproduction

```js
import { spotlight } from '@mantine/spotlight';

// Open the spotlight
spotlight.open();

// Close it
spotlight.close();
// The close action gets called twice internally
```

When you call `spotlight.close()`, it seems to execute the close action multiple times, which can lead to issues if you have cleanup logic or event handlers attached to the close event.

### Expected behavior

The `spotlight.close()` method should only close the spotlight once per call, not trigger the close action multiple times.

### System Info
- @mantine/spotlight version: latest
- Browser: Chrome/Firefox

---
Repository: /testbed
