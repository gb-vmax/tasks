# Bug Report

### Describe the bug

After a recent update, the markdown parser appears to be completely broken. When trying to parse any markdown content, the parser fails to process the input and doesn't produce any output or throws errors.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Hello World

This is a test document with **bold** text.
`;

const result = remark().processSync(markdown);
console.log(result);
```

### Expected behavior

The parser should successfully process the markdown input and return the parsed AST or transformed output. Previously this was working fine, but now it seems like the tokenizer is not functioning correctly.

### Additional context

This seems to affect all markdown parsing operations. Even simple documents fail to parse. The issue appeared suddenly and I haven't changed any configuration on my end.

---
Repository: /testbed
