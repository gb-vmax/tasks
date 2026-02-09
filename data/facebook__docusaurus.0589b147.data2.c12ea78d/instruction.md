# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in MDX. When processing headings with certain content patterns, the parser seems to enter an infinite loop or hang indefinitely. The page becomes unresponsive and never finishes rendering.

### Reproduction

```mdx
# Heading with some text

## Another heading
```

When parsing documents with ATX-style headings (using `#` syntax), the parser appears to get stuck and doesn't complete. This happens with both single and multiple headings in the document.

### Expected behavior

The MDX parser should successfully parse ATX headings and return the processed output without hanging. The headings should be tokenized correctly and the parsing should complete in a reasonable time.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest
- Browser: Chrome/Firefox (both affected)

This seems to have started recently. Any headings in my MDX files are causing the application to freeze. Would appreciate any help debugging this!

---
Repository: /testbed
