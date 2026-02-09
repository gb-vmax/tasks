# Bug Report

### Describe the bug

I'm encountering an issue with nested curly braces in MDX expressions. When I try to use objects or nested structures inside MDX expressions, the parser seems to get confused and doesn't properly handle the closing braces.

### Reproduction

```mdx
{/* This should work but doesn't parse correctly */}
{someFunction({ nested: { value: 'test' } })}

{/* Also fails with object literals */}
{{ key: 'value' }}
```

The parser appears to be closing the expression too early when it encounters the first closing brace, even when there are still unclosed opening braces.

### Expected behavior

The parser should correctly match opening and closing braces, allowing for nested objects and function calls with object parameters inside MDX expressions. The expression should only close when all braces are properly balanced.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
