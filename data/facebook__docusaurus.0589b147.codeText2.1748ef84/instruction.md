# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX. When using backticks for inline code in my MDX files, the code is not being rendered correctly. It seems like the AST node structure has changed unexpectedly.

### Reproduction

```mdx
This is some text with `inline code` that should be formatted.
```

When this MDX is processed, the inline code blocks are not being recognized or rendered properly. The output doesn't show the inline code with the expected formatting.

### Expected behavior

Inline code wrapped in backticks should be properly parsed and rendered as inline code elements. The AST should generate nodes with type `"inlineCode"` and a `value` property containing the code text.

### Additional context

This appears to have started recently. The inline code syntax worked fine before, but now it's producing unexpected output or failing to render the inline code sections at all.

---
Repository: /testbed
