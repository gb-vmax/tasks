# Bug Report

### Describe the bug

I'm encountering an issue with the remark-gfm syntax extension handling where construct additions are being placed in the wrong order. When adding constructs with specific placement requirements (using the `add` property), they're not being inserted into the correct position in the extension list.

### Reproduction

```js
const extension = {
  constructs: [
    { add: 'before', /* ... */ },
    { add: 'after', /* ... */ },
    { /* no add property */ }
  ]
};

// After processing, constructs with add: 'before' are being 
// added to the main list instead of the before array,
// and constructs with add: 'after' or no add property 
// are being placed incorrectly
```

### Expected behavior

Constructs should be organized as follows:
- Items with `add: 'before'` should be collected in the `before` array and spliced at the beginning
- Items with `add: 'after'` or no `add` property should be added to the existing array
- The final order should respect these placement requirements

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This is causing syntax extensions to be processed in the wrong order, which breaks certain markdown parsing scenarios that depend on construct precedence.

---
Repository: /testbed
