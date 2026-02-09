# Bug Report

### Describe the bug

I'm encountering an issue with token parsing where the token stack appears to get corrupted during markdown processing. After parsing certain markdown structures, tokens that should have been popped from the stack are still present, causing subsequent parsing operations to fail or produce incorrect results.

### Reproduction

```js
const parser = createTokenizer(/* ... */);

// Parse markdown with nested structures
const result = parser.parse(`
# Header
- List item 1
- List item 2
`);

// The token stack has extra tokens that shouldn't be there
// Expected stack to be empty or contain only root tokens
// Actual: contains already-exited tokens
```

### Expected behavior

When a token is exited, it should be removed from the stack and not be present for subsequent parsing operations. The stack should only contain currently active/open tokens.

### Additional context

This seems to affect parsing of nested markdown structures like lists within blockquotes, or emphasis within links. The parser state gets confused and either produces malformed AST nodes or throws errors about unexpected token types.

Not sure when this started happening, but it's making it difficult to parse complex markdown documents correctly.

---
Repository: /testbed
