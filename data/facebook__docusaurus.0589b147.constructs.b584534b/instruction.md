# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-gfm parser where it seems to be accessing array elements out of bounds and inserting constructs at the wrong position. This is causing unexpected behavior when parsing GFM markdown extensions.

### Reproduction

When processing markdown with custom syntax extensions, the parser appears to be iterating one index too far in the constructs array and then splicing at an incorrect position. This leads to:

1. Potential access of `undefined` array elements (when `index` equals `list2.length`)
2. Constructs being inserted at the wrong location in the existing array

```js
// Example that triggers the issue
const list = [
  { add: "before", /* ... */ },
  { add: "after", /* ... */ }
];

// The loop accesses list[list.length] which is undefined
// Then splices at the wrong offset
```

### Expected behavior

The constructs should be properly collected and inserted at the beginning of the existing array (index 0), not at an offset equal to the before array length. The loop should also stop at `index < list2.length` to avoid accessing undefined elements.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This seems like it could cause issues with markdown parsing when multiple extensions are registered. Has anyone else encountered this?

---
Repository: /testbed
