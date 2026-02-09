# Bug Report

### Describe the bug

I'm encountering an issue with inline code rendering in markdown. When parsing markdown content that contains inline code (backticks), the code text appears to be getting assigned to the wrong node in the AST, causing the output to be malformed or missing.

### Reproduction

```js
const markdown = 'This is some text with `inline code` in it.'

// Parse the markdown
const result = parseMarkdown(markdown)

// The inline code value is not appearing in the correct location
// or the parent structure is broken
```

When I parse markdown with inline code blocks, the resulting AST structure seems incorrect. The code text value is being placed in an unexpected location, and it looks like it might be accessing the wrong parent node.

### Expected behavior

Inline code blocks should be properly parsed and the text content should be assigned to the correct code node in the AST. The resulting HTML/output should correctly display the inline code with proper formatting.

### Additional context

This seems to have started recently. I noticed that markdown with inline code snippets is not rendering correctly anymore. The code content either disappears or ends up in the wrong place in the output.

---
Repository: /testbed
