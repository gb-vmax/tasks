# Bug Report

### Describe the bug

I'm encountering a critical issue where MDX expression parsing appears to be completely broken. When trying to process MDX files with expressions, the parser crashes or produces invalid output.

### Reproduction

```js
// Any MDX file with expressions fails to parse
const mdxContent = `
# Hello

{someExpression}

Some text with {inlineExpression} here.
`

// Parser fails when processing this content
```

### Expected behavior

MDX expressions should be parsed correctly and the `exitMdxExpressionData` function should handle the token data properly. The parser should process expressions without errors.

### Additional context

This seems to have broken recently. Previously, expressions in MDX files were working fine, but now they're causing the parser to fail completely. It looks like something fundamental changed in how expression data is being handled.

---
Repository: /testbed
