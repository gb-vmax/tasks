# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where closing braces `}` are being consumed even when they shouldn't be. It seems like the parser is not properly checking if the expression is balanced before closing it.

### Reproduction

When writing MDX with nested braces in expressions, the parser incorrectly treats the first closing brace as the end of the expression, even when there are still open braces that need to be matched.

For example:
```mdx
{someFunction({ nested: 'object' })}
```

The parser appears to close the expression at the first `}` (after `'object'`) instead of waiting for the final closing brace. This causes the rest of the content to be treated incorrectly.

### Expected behavior

The parser should track the nesting level of braces and only close the MDX expression when all braces are properly balanced (i.e., when `size === 0`). It should not consume a closing brace if there are still unmatched opening braces in the expression.

### Additional context

This seems to have started happening recently. The expression parsing logic should be checking the `size` variable to ensure proper brace matching before deciding to close an expression.

---
Repository: /testbed
