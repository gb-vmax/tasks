# Bug Report

### Describe the bug

The spotlight close action seems to be checking state conditions before closing, which causes issues when trying to close the spotlight in certain scenarios. The close function now has conditional logic that prevents it from executing properly.

### Reproduction

```js
import { spotlight } from '@mantine/spotlight';

// Open the spotlight
spotlight.open();

// Try to close it immediately
spotlight.close();
// Expected: spotlight closes
// Actual: spotlight may not close depending on internal state
```

When calling `spotlight.close()` multiple times in quick succession or in certain timing scenarios, the spotlight doesn't close as expected. This appears to be related to the state checking logic that was added.

### Expected behavior

The `spotlight.close()` method should always close the spotlight when called, regardless of internal state conditions. It should behave consistently like the `open()` method does.

### System Info
- @mantine/spotlight version: latest
- React version: 18.x

---
Repository: /testbed
