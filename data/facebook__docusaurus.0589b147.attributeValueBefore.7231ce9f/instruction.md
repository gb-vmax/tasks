# Bug Report

### Describe the bug

MDX attribute values with single quotes are not being parsed correctly. When I try to use single-quoted attribute values in JSX tags within MDX files, the parser crashes with an error message instead of accepting the valid syntax.

### Reproduction

```mdx
<Component name='test' />
```

Or with double quotes:

```mdx
<Component name="test" />
```

### Expected behavior

Both single quotes (`'`) and double quotes (`"`) should be valid for attribute values in JSX/MDX syntax, just like in regular JSX. The parser should accept either format without crashing.

### Additional context

This seems to affect all attribute values using quoted strings. The parser appears to reject the quotes entirely rather than treating them as valid delimiters for string values.

---
Repository: /testbed
