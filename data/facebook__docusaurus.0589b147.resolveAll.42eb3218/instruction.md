# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs are not being resolved correctly. It seems like the resolver functions are being skipped or not applied properly, resulting in malformed output for some markdown patterns.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Heading

Some **bold** text with [links](http://example.com) and other constructs.

- List item 1
- List item 2
`;

const result = remark().processSync(markdown);
console.log(result);
```

When processing markdown with multiple constructs that need resolution, some of them don't get processed at all. The output is missing expected transformations that should have been applied.

### Expected behavior

All registered resolver functions should be called and applied to the markdown constructs. Each unique resolver should process the events exactly once to produce the correct output.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
