# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where the label link tokens are being entered/exited in the wrong order. This causes the AST (Abstract Syntax Tree) to have an incorrect structure when parsing markdown links.

### Reproduction

When parsing markdown with links like `[text](url)`, the tokenizer appears to be calling `effects.exit("labelLink")` before `effects.enter("labelLink")`, which results in an unbalanced token stream.

```js
// Parsing markdown with a simple link
const markdown = '[example](https://example.com)'
const result = parseMarkdown(markdown)

// The AST structure is malformed due to incorrect token ordering
console.log(result) // Shows exit before enter for labelLink
```

### Expected behavior

The tokenizer should properly enter the `labelLink` token before exiting it, maintaining the correct nesting structure:
1. Enter labelLink
2. Enter labelMarker
3. Consume code
4. Exit labelMarker  
5. Exit labelLink

This ensures the AST has the proper hierarchical structure for downstream processing.

### Additional context

This seems to affect any markdown content with link syntax. The token stream becomes unbalanced which could cause issues with any tools or parsers that depend on properly nested tokens.

---
Repository: /testbed
