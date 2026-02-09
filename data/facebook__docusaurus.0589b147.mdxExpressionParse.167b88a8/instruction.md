# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where syntax errors in expressions are not being properly reported. When I write invalid MDX expressions, they seem to be silently accepted instead of throwing errors as expected.

### Reproduction

```mdx
{...props, extraProp}
```

When using a spread with multiple properties like above, the parser doesn't report an error even though only a single spread should be supported according to the spec.

Also, when writing expressions with syntax errors:

```mdx
{invalid javascript syntax here}
```

The parser seems to accept these invalid expressions instead of reporting parse errors.

### Expected behavior

1. Expressions with multiple properties in a spread should throw an error indicating that only a single spread is supported
2. Invalid JavaScript syntax in expressions should be reported as parse errors with proper error messages and location information

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
