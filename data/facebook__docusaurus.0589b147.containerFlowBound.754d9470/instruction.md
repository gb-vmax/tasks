# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where container flow elements are not being processed correctly. It seems like the parsed output is missing or incomplete when dealing with flow content inside containers.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
> This is a blockquote
> 
> With multiple paragraphs
`;

const result = processor.processSync(markdown);
console.log(result);
```

When parsing markdown with container flow elements (like blockquotes with multiple paragraphs), the output appears to be undefined or not returning the expected result. The container structure seems to be processed but the return value is lost.

### Expected behavior

The processor should return the properly parsed AST with all container flow elements intact and accessible.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
