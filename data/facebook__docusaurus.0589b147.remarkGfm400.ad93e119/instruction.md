# Bug Report

### Describe the bug
I'm encountering an issue with the remark-gfm plugin where it crashes when `data.micromarkExtensions` is undefined. The plugin tries to call `push()` on an undefined value, which throws an error.

### Reproduction
```js
const unified = require('unified');
const remarkGfm = require('remark-gfm');

const processor = unified()
  .use(remarkGfm)
  .freeze();

// This throws: Cannot read property 'push' of undefined
```

The error occurs because the code tries to push to `micromarkExtensions` after checking if it exists, but doesn't actually initialize the array when it's undefined.

### Expected behavior
The plugin should properly initialize `data.micromarkExtensions` as an empty array if it doesn't exist, similar to how `fromMarkdownExtensions` and `toMarkdownExtensions` are handled.

### Additional context
This seems to happen when the processor's data object doesn't have `micromarkExtensions` pre-initialized. The current code checks for the existence but doesn't assign the empty array back to the data object.

---
Repository: /testbed
