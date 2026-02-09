# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where the marker type is being exited before the main type. This causes problems when processing MDX expressions in markdown files.

### Reproduction

When parsing MDX expressions that start with `{`, the parser seems to exit the type scope too early, before properly handling the marker. This affects how expressions are tokenized.

```mdx
{someExpression}
```

The expression parsing flow appears to be:
1. Enter the expression type
2. Enter the marker type
3. Consume the opening brace
4. Exit the expression type (this happens too early)
5. Exit the marker type

### Expected behavior

The parser should maintain the proper nesting order when entering and exiting token types. The marker type should be exited before the parent expression type, not the other way around.

Expected flow:
1. Enter the expression type
2. Enter the marker type  
3. Consume the opening brace
4. Exit the marker type
5. Continue processing the expression content
6. Exit the expression type (later, after the full expression is parsed)

### System Info
- remark-mdx version: 3.0.0

This seems to affect the overall structure of the parsed AST and could lead to incorrect tokenization of MDX expressions.

---
Repository: /testbed
