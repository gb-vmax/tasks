# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in MDX content. When processing fenced code blocks, the parser seems to get stuck in an infinite loop or produces incorrect token output. This appears to be related to how line endings are handled in the closing fence of code blocks.

### Reproduction

```mdx
# Test Document

```js
const example = 'test';
```

More content here
```

When parsing this MDX content, the parser doesn't correctly handle the closing fence of the code block. The issue seems to occur specifically when processing the line ending before the closing backticks.

### Expected behavior

The parser should correctly tokenize the entire code fence, including both opening and closing delimiters, and continue parsing the rest of the document normally. The closing fence should be properly recognized and the parser should exit the code block context.

### Additional context

This started happening recently and affects all fenced code blocks in MDX documents. The problem seems to be in the tokenization logic for code fence closures.

---
Repository: /testbed
