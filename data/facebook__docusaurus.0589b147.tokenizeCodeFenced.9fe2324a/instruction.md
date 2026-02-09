# Bug Report

### Describe the bug

I'm experiencing issues with fenced code blocks in markdown parsing. It seems like code blocks with certain fence configurations are not being properly recognized or closed.

### Reproduction

```markdown
```js
console.log('test')
```
```

When parsing the above markdown with a fenced code block, the block doesn't get properly recognized in some edge cases. Specifically:

1. Code blocks with no indentation/prefix seem to have issues
2. Closing fences that are the exact same length as opening fences may not be detected correctly

### Expected behavior

Fenced code blocks should be properly parsed regardless of:
- Whether there's any prefix/indentation (including zero indentation)
- Whether the closing fence is exactly the same length as the opening fence

The parser should correctly identify both the start and end of fenced code blocks in these scenarios.

### Additional context

This appears to affect the tokenization logic for code fences. The issue manifests when trying to parse markdown documents with fenced code blocks that have specific fence length configurations.

---
Repository: /testbed
