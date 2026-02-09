# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content chunks are not being processed correctly. It appears that the tokenizer is skipping over content or not properly linking chunks together during parsing.

### Reproduction

When parsing markdown with multiple content chunks, the parser seems to be jumping to the wrong state or not maintaining the proper chain of content nodes. This causes some content to be lost or incorrectly structured in the output.

```js
const markdown = `
Some paragraph text here.

Another paragraph with more content.
`;

// Parse the markdown
const result = remark().parse(markdown);

// Expected: Both paragraphs should be present in the AST
// Actual: Content appears to be missing or improperly linked
```

### Expected behavior

The tokenizer should properly process all content chunks in sequence, maintaining the correct chain of previous/next references between chunks. Each chunk should be fully processed before moving to the next one.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have broken recently - the content tokenization logic might have been changed in a way that affects how chunks are connected or how the state machine transitions work.

---
Repository: /testbed
