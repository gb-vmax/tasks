# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where syntax extensions are not being processed in the correct order. When I define custom syntax constructs with `add: "after"` or `add: "before"` properties, they appear to be added in the wrong position or skipped entirely.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const customExtension = {
  add: 'after',
  // ... other properties
};

const result = await mdx.compile(content, {
  remarkPlugins: [
    // plugin that uses the extension
  ]
});
```

When processing the syntax extensions, constructs that should be added "after" existing ones are being placed "before" instead, and the first construct in the list seems to be getting skipped during iteration.

### Expected behavior

Syntax extensions with `add: "after"` should be appended to the existing constructs list, while those with `add: "before"` (or no `add` property) should be prepended. All constructs in the provided list should be processed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
