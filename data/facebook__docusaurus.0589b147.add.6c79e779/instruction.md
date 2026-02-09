# Bug Report

### Describe the bug

When trying to use plugins with the remark processor, I'm getting unexpected behavior. It seems like non-function values are being treated as plugins when they shouldn't be, and function values are being rejected.

### Reproduction

```js
const remark = require('remark');

const processor = remark();

// This should work but doesn't
processor.use(myPluginFunction);

// This incorrectly accepts non-function values
processor.use("not a plugin");
```

### Expected behavior

The processor should accept function plugins and properly validate the input types. Functions should be recognized as valid plugins, while non-function primitives (like strings) should throw a TypeError.

### Additional context

This appears to have broken recently. The type checking logic seems to be inverted - it's rejecting functions and accepting non-functions when it should be doing the opposite.

---
Repository: /testbed
