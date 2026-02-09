# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-rehype transformer where the output structure is incorrect when converting markdown to HAST. The resulting tree structure appears to be malformed - it seems like the logic for handling array vs non-array nodes got inverted somehow.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');

const processor = unified()
  .use(remarkParse)
  .use(remarkRehype);

const markdown = `
# Hello World

This is a test.
`;

const result = processor.processSync(markdown);
console.log(result);
```

### Expected behavior

The transformer should correctly wrap non-array nodes in a root object with a `children` property, and handle array nodes appropriately. Currently, it appears to be doing the opposite - wrapping array nodes instead of non-array nodes.

Also, footnotes/footer content should be appended to the children when present, but they seem to be getting skipped or added at the wrong times.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
