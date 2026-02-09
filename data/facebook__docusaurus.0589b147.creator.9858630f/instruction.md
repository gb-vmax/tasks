# Bug Report

### Describe the bug

I'm encountering an issue with the remark parser where tokenization is not working correctly. It seems like the parser is not properly handling the initial state when creating tokenizers, causing parsing to fail or produce incorrect results.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Test heading

Some paragraph text.
`;

const processor = remark().parse(markdown);
console.log(processor);
```

When running this, the parser doesn't correctly process the markdown. The tokenizer seems to be initialized with the wrong parameters, leading to unexpected parsing behavior.

### Expected behavior

The markdown should be parsed correctly with proper tokenization. The initial state should be passed to the tokenizer so that it can properly track parsing position and context.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
