# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX. When processing fenced code blocks, the parser seems to be handling line endings incorrectly, which causes the tokenization to fail or produce unexpected results.

### Reproduction

```mdx
# Test Document

```javascript
const foo = 'bar';
```

More content here
```

When parsing this MDX content, the code fence closing sequence is not being recognized properly. The tokenizer appears to be exiting the "lineEnding" token before entering it, which breaks the expected token flow.

### Expected behavior

Code fences should be properly tokenized with correct line ending handling. The opening and closing fence sequences should both be recognized, and the content between them should be treated as code.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - code fences were working fine before. Not sure if this is related to a recent change in the tokenization logic.

---
Repository: /testbed
