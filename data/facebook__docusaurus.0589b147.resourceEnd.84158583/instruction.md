# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with resources are not being properly closed. It seems like the parser is accepting malformed link syntax that should be rejected.

### Reproduction

```markdown
[link](url "title"
```

When parsing the above markdown (note the missing closing parenthesis), the parser appears to accept it as valid when it should reject this malformed syntax.

### Expected behavior

The parser should reject markdown links that don't have a proper closing parenthesis `)` for the resource section. Links must be properly closed to be valid markdown syntax.

### Additional context

This affects link parsing behavior and could lead to unexpected results when processing markdown documents with malformed links. The parser should be stricter about validating the closing marker for link resources.

---
Repository: /testbed
