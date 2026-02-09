# Bug Report

### Describe the bug

I'm encountering an issue with nested curly braces in MDX expressions. When using curly braces inside an expression (like for object literals or nested structures), the parser seems to be getting confused about when the expression actually ends.

### Reproduction

```mdx
{
  const obj = { nested: { value: 'test' } }
}
```

Or when trying to use object destructuring:

```mdx
{ const { a, b } = props }
```

The parser appears to close the expression prematurely or incorrectly track the brace depth, causing parsing errors or unexpected behavior.

### Expected behavior

The parser should correctly handle nested curly braces within MDX expressions, properly tracking opening and closing braces to determine when the expression actually ends. Nested objects, destructuring, and other JavaScript syntax using curly braces should work without issues.

### Additional context

This seems to affect any MDX expression that contains curly braces as part of the JavaScript syntax itself (not just the expression delimiters). The issue might be related to how the brace counter is being incremented/decremented.

---
Repository: /testbed
