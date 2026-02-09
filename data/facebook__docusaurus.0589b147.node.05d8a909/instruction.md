# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content is not being processed correctly. It seems like nodes in the markdown AST are not being recognized properly, causing the parser to skip over valid markdown structures.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Hello World

This is a paragraph with **bold** text.

- List item 1
- List item 2
`;

const result = processor.processSync(markdown);
console.log(result.toString());
```

### Expected behavior

The markdown should be parsed and processed normally, with all nodes (headings, paragraphs, lists, etc.) being recognized and handled correctly. Instead, it appears that the node validation is failing and content is being ignored or not processed as expected.

### Additional context

This seems to have started happening recently. The markdown content that used to work fine is now not being parsed correctly. I suspect there might be an issue with how nodes are being validated internally, but I'm not entirely sure what changed.

---
Repository: /testbed
