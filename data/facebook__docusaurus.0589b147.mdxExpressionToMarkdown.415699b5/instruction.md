# Bug Report

### Describe the bug

After a recent update, MDX expression rendering appears to be completely broken. When trying to use MDX expressions in markdown files (both inline `{expression}` and block-level expressions), they no longer render correctly and the output is corrupted.

### Reproduction

```mdx
# Test Document

This is a test with an inline expression: {variable}

{
  // Block expression
  someValue
}
```

When processing this MDX content, the expressions are not being serialized properly. Instead of getting valid markdown output with the expressions preserved, the serialization seems to fail or produce unexpected results.

### Expected behavior

MDX expressions (both `mdxFlowExpression` and `mdxTextExpression`) should be properly converted to markdown format. The serialization should handle:
- Inline expressions like `{variable}`
- Block-level expressions
- Proper escaping of `{` characters in different contexts

### Additional context

This seems to have started happening recently. The MDX expression handling in the remark-mdx plugin appears to be affected. When converting from MDX AST back to markdown, the expressions are not being processed at all.

---
Repository: /testbed
