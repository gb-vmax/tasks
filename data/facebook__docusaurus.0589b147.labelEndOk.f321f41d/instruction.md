# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links are not being processed correctly. The parser seems to be breaking when it encounters certain link structures, and the output is not what I'd expect.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
Check out [this link](https://example.com) for more info.
`;

const result = processor.processSync(markdown);
console.log(result);
```

When I run this, the link isn't being parsed properly. It seems like the tokenizer is returning `true` instead of the actual result, which causes the link processing to fail.

### Expected behavior

Links should be tokenized and processed correctly, with the parser returning the proper AST structure for the link nodes.

### System Info
- remark version: 15.0.1
- Node version: Latest

Has anyone else run into this? It was working fine before but something seems to have changed with how the label end tokens are being handled.

---
Repository: /testbed
