# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in markdown. When I have inline code blocks (using backticks) in my markdown content, the parsed output seems to be corrupted or assigned to the wrong node in the AST.

### Reproduction

```js
const markdown = 'This is some text with `inline code` in it.';
// Process the markdown
const result = processor.parse(markdown);
```

When parsing markdown containing inline code (text wrapped in backticks), the resulting AST structure appears to be malformed. The code value seems to end up in an unexpected location in the node tree, and the structure doesn't match what's expected for inline code elements.

### Expected behavior

Inline code should be properly parsed and the value should be assigned to the correct node in the AST. The structure should maintain proper parent-child relationships for inline code elements.

### Additional context

This seems to affect any markdown content that contains inline code using backticks. Regular code blocks (using triple backticks) might be fine, but single backtick inline code is definitely broken.

---
Repository: /testbed
