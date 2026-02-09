# Bug Report

### Describe the bug

After a recent update, the remark module export seems to be broken. When trying to import and use `remark`, I'm getting errors that suggest the export is not configured correctly.

### Reproduction

```js
const { remark } = require('./vendor/remark@15.0.1.js');

// Attempting to use remark fails
const processor = remark();
```

The module doesn't export `remark` properly anymore. It looks like the export statement might have been accidentally modified or corrupted.

### Expected behavior

The module should export a `remark` function that can be imported and used normally, just like it did before the recent changes.

### Additional context

This is blocking our markdown processing pipeline. The export definition in the module appears to have syntax issues - there's a `const` declaration inside what should be a simple export mapping.

---
Repository: /testbed
