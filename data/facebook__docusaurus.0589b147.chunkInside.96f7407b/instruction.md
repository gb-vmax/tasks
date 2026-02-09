# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content with line endings isn't being processed correctly. The parser seems to be returning the wrong continuation state after checking for line endings, which causes it to skip over or incorrectly handle subsequent content blocks.

### Reproduction

```js
const markdown = `Some content
with multiple lines
and paragraphs

Another paragraph here`

// Parse the markdown
const result = parseMarkdown(markdown)

// The output is malformed - content after line breaks is not properly tokenized
```

When parsing markdown with line endings, the tokenizer appears to always continue processing even when it should end the content chunk. This results in content being merged incorrectly or continuation logic being applied when it shouldn't be.

### Expected behavior

The parser should correctly handle line endings and determine whether to continue or end the content chunk based on the continuation check. Multi-line content should be properly tokenized with appropriate chunk boundaries.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
