# Bug Report

### Describe the bug

When using MDX expressions with nested curly braces, the parser doesn't handle the closing brace correctly. Expressions that contain nested objects or code blocks with curly braces get terminated prematurely, causing parsing errors or unexpected behavior.

### Reproduction

```mdx
{
  {
    nested: 'value'
  }
}
```

The parser seems to close the expression at the first `}` instead of waiting for the matching closing brace. This breaks when trying to use inline objects or any JavaScript code that contains nested braces.

Another example that fails:
```mdx
{someFunction({ param: 'test' })}
```

### Expected behavior

The parser should correctly track nested curly braces and only close the MDX expression when it encounters the matching closing brace. Nested braces within the expression should be handled properly without prematurely terminating the expression.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
