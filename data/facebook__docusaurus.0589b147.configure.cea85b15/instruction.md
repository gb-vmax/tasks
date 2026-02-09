# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where extensions are not being applied correctly. It seems like the last extension in the array is being skipped when configuring the parser.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

const extensions = [
  { name: 'extension1' },
  { name: 'extension2' },
  { name: 'extension3' }
];

// Only the first two extensions are processed
// extension3 is never applied
const result = await compile(content, {
  remarkPlugins: extensions
});
```

When I pass multiple extensions, the last one in the array doesn't get processed. This is causing some of my custom plugins to be ignored completely.

### Expected behavior

All extensions in the array should be processed and applied to the MDX compiler, including the last one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
