# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where attribute values with curly braces `{}` are not being recognized correctly. When I try to use expression syntax for attribute values in MDX components, the parser seems to be rejecting valid syntax.

### Reproduction

```mdx
<MyComponent prop={someValue} />
```

When trying to parse the above MDX code, I get an error about the attribute value format. The parser appears to be expecting something different when it encounters the opening curly brace for the expression.

### Expected behavior

The parser should correctly handle JSX-style expression attributes with curly braces. This is standard MDX/JSX syntax and should work for passing dynamic values or expressions as props to components.

### Additional context

This seems to affect any component attribute that uses expression syntax. String literals with quotes work fine, but as soon as I try to use `{...}` for an expression, the parsing fails.

---
Repository: /testbed
