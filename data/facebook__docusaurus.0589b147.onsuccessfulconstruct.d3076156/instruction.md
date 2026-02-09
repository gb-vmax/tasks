# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the parser seems to be passing arguments in the wrong order internally. This is causing unexpected behavior when processing markdown content with certain constructs.

### Reproduction

When parsing markdown documents with specific syntax constructs, the parser fails to properly handle the tokenization process. The issue appears to be related to how construct information is being processed during successful token construction.

```js
// Example markdown content that triggers the issue
const markdown = `
# Heading
Some text with **bold** and *italic*
`;

const result = remark().parse(markdown);
// Parser produces incorrect or incomplete AST
```

### Expected behavior

The markdown parser should correctly tokenize and construct the AST for all valid markdown syntax. Arguments should be passed to internal functions in the correct order to ensure proper processing.

### System Info
- remark version: 15.0.1
- Node version: Latest

The parsing behavior was working correctly before, but now certain markdown constructs are not being processed as expected. This seems to be an internal issue with how the tokenizer handles successful construct callbacks.

---
Repository: /testbed
