# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where paragraph content is being processed before the paragraph token is properly initialized. This is causing the content to be parsed outside of its expected paragraph container.

### Reproduction

When parsing markdown text that starts with a paragraph, the text chunks are being entered before the paragraph token itself is entered. This breaks the expected AST structure where paragraph content should be nested within the paragraph node.

```markdown
This is a simple paragraph.
```

The expected token sequence should be:
1. Enter paragraph token
2. Enter/process line content
3. Exit paragraph token

But currently the line content is being processed before the paragraph token is entered.

### Expected behavior

The paragraph token should be entered before any of its child content tokens are processed. This ensures proper nesting in the syntax tree and maintains the correct parent-child relationships in the AST.

### Additional context

This affects any markdown content that begins with paragraph text and likely impacts downstream processors that rely on the correct token ordering for parsing and transforming markdown documents.

---
Repository: /testbed
