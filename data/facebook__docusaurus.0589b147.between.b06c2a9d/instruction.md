# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX where spaces immediately after the opening backticks are not being handled correctly. The parser seems to be consuming spaces in a way that breaks the code text tokenization.

### Reproduction

```mdx
This is `code with space` in text.
```

When parsing inline code that starts with a space (like `` ` code` ``), the tokenizer doesn't properly track the sequence state and the space gets treated as data instead of being part of the spacing logic.

### Expected behavior

Spaces after opening backticks should be properly handled during tokenization, and the parser should correctly identify the code text boundaries regardless of leading/trailing spaces.

### Additional context

This appears to be related to the `tokenizeCodeText` function in the MDX parser. The issue manifests when:
1. An inline code block is opened with backticks
2. There's a space immediately following the opening sequence
3. The parser needs to determine whether to continue in "between" state or transition to data

The current behavior causes incorrect state transitions which can lead to malformed AST output or parsing errors.

---
Repository: /testbed
