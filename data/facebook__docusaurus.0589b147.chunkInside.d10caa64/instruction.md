# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content processing seems to hang or behave unexpectedly when encountering certain input patterns. The parser appears to get stuck in an infinite loop or doesn't properly terminate when processing chunks of content.

### Reproduction

```js
const remark = require('remark');

const markdown = `
Some content here
`;

// Parser seems to hang or not terminate properly
const result = remark().parse(markdown);
```

The issue appears to be related to how the content tokenizer handles the end of input. When processing markdown content that should terminate normally, the parser doesn't exit cleanly.

### Expected behavior

The parser should properly detect the end of content and terminate the tokenization process without hanging or entering an infinite loop. All markdown input should be processed and returned correctly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
