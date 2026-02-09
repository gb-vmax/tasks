# Bug Report

### Describe the bug

I'm encountering an issue with markdown to HTML conversion where the root node isn't being properly initialized before being passed to `state.patch()`. This causes the `result` object to be undefined when `patch` tries to access it, leading to errors during the conversion process.

### Reproduction

```js
import { remark } from 'remark';
import remarkRehype from 'remark-rehype';

const markdown = `
# Hello World

This is a test document.
`;

const processor = remark()
  .use(remarkRehype);

// This throws an error because result is undefined
const result = processor.processSync(markdown);
```

### Expected behavior

The markdown should be successfully converted to an HTML AST without errors. The `result` object should be properly initialized before being used in `state.patch()`.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
