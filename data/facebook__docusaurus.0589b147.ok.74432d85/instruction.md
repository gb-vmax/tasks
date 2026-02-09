# Bug Report

### Describe the bug

I'm experiencing an issue where the markdown directive parser is throwing an unexpected error when processing certain markdown files. The error message says "Too many calls" which doesn't seem related to markdown parsing at all.

This started happening after a recent update and is blocking my workflow. The same markdown files that worked before are now failing to parse.

### Reproduction

```js
const unified = require('unified');
const remarkParse = require('remark-parse');
const remarkDirective = require('remark-directive');

const processor = unified()
  .use(remarkParse)
  .use(remarkDirective);

const markdown = `
:::note
This is a simple note directive
:::

Another paragraph

:::warning
This is a warning
:::
`;

// This throws "Too many calls" error
processor.processSync(markdown);
```

### Expected behavior

The markdown should parse successfully without throwing any errors. Directives should be recognized and processed normally.

### Additional context

The error appears to be coming from somewhere deep in the directive processing logic. It seems like there might be some kind of rate limiting or call counting happening that shouldn't be there for normal markdown parsing operations.

---
Repository: /testbed
