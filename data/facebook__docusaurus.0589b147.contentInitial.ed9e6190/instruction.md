# Bug Report

### Describe the bug

After a recent update, the MDX parser is failing to process content correctly. The `contentInitial` export seems to have been replaced with a more complex structure that's breaking existing code that depends on it.

### Reproduction

```js
import { contentInitial } from '@mdx-js/mdx';

// This used to work but now fails
const content = contentInitial();
```

The error occurs because `contentInitial` is no longer directly exported as a function. Instead, it appears to be wrapped in some kind of manager object, but the export statement still references `contentInitial` directly which causes issues when trying to use it.

### Expected behavior

The `contentInitial` function should be callable directly after importing, just like it was before. The parser should initialize content without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
