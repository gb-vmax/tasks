# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link titles not being parsed correctly. When I create a link with a title attribute, the title doesn't appear in the rendered output or in the parsed AST node.

### Reproduction

```markdown
[link text](https://example.com "This is a title")
```

When parsing the above markdown, the title "This is a title" is not being assigned to the correct node property. Instead of appearing as the link's title, it seems to be going somewhere else entirely.

### Expected behavior

The parsed link node should have a `title` property containing "This is a title". The title should be accessible and properly rendered when the markdown is processed.

### Additional context

This appears to affect all links with title strings in the resource notation (the part in parentheses after the link text). Links without titles seem to work fine, but as soon as you add a title string in quotes, it gets misplaced in the AST.

---
Repository: /testbed
