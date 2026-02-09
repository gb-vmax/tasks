# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports in the vendored `mdast-util-to-string` library. The exported properties are no longer accessible as expected, causing runtime errors when trying to use the module's functionality.

### Reproduction

```js
// Attempting to import and use mdast-util-to-string
import { toString } from 'mdast-util-to-string';

const tree = {
  type: 'paragraph',
  children: [{type: 'text', value: 'hello'}]
};

// This fails with an error about missing/inaccessible exports
const result = toString(tree);
```

### Expected behavior

The module should export its functions correctly and they should be accessible for use. Properties should be enumerable so they can be properly imported and utilized.

### Additional context

This seems to have started after changes to the vendor bundle. The exports are being defined but they're not behaving as standard ES module exports should.

---
Repository: /testbed
