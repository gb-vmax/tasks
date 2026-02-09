# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in MDX. When parsing fenced code blocks, the parser seems to be entering the `codeFencedFence` state twice, which causes problems with the tokenization process.

### Reproduction

```markdown
```js
const example = 'test';
```
```

When this markdown is parsed, the fence tokens are not being created correctly. The parser appears to duplicate the fence entry, leading to incorrect AST structure.

### Expected behavior

The parser should correctly tokenize the code fence by entering the `codeFencedFence` state only once during the opening sequence. The resulting AST should have the proper structure for rendering the fenced code block.

### Additional context

This seems to affect any fenced code block regardless of the language identifier or content. The issue appears to be in the tokenization logic where the fence sequence is being processed.

---
Repository: /testbed
