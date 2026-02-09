# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where curly braces inside expressions are not being balanced correctly. When I have nested braces in my MDX expressions, the parser seems to get confused and doesn't properly track the opening and closing braces.

### Reproduction

```mdx
{someFunction({ nested: 'value' })}
```

When using expressions with nested object literals or function calls that contain braces, the parser doesn't handle them properly. It appears that the brace counting logic isn't working as expected, especially when dealing with nested structures.

### Expected behavior

The parser should correctly balance opening `{` and closing `}` braces even when they're nested within expressions. Expressions like `{foo({ bar: 'baz' })}` should be parsed without issues.

### Additional context

This seems to affect any MDX expression that contains nested braces, including:
- Object literals inside expressions
- Function calls with object arguments
- Nested destructuring patterns

The parser should maintain proper brace counting to determine when an expression actually ends.

---
Repository: /testbed
