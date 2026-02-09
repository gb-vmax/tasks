# Bug Report

### Describe the bug

After a recent update, code fences in MDX files are not being parsed correctly. The parser seems to exit prematurely when processing fenced code blocks, causing the content to not be recognized as code.

### Reproduction

```mdx
# Test Document

```js
const example = 'test';
console.log(example);
```

Some text after the code block.
```

When parsing the above MDX content, the code fence is not properly recognized and the JavaScript code is treated as regular text instead of a code block.

### Expected behavior

The fenced code block should be properly parsed and tokenized. The content between the backticks should be identified as code with the language info (`js`) preserved, and subsequent content should be treated as normal markdown text.

### Additional context

This appears to affect all fenced code blocks regardless of the language specified. The issue seems related to how the fence info (language identifier) is being processed during tokenization.

---
Repository: /testbed
