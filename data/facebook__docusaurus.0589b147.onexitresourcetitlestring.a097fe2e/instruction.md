# Bug Report

### Describe the bug
When parsing markdown links with titles, the title is being set on the wrong node in the AST. Instead of setting the title on the immediate parent node (the link node), it's being set two levels up in the stack, which causes the title to either be placed incorrectly or lost entirely.

### Reproduction
```markdown
[link text](https://example.com "Link Title")
```

When parsing this markdown, the link title "Link Title" should be attached to the link node itself, but it appears to be getting attached to a parent node instead.

### Expected behavior
The title should be properly attached to the link node in the AST. When accessing the parsed link node, `node.title` should contain "Link Title".

### Additional context
This seems to affect resource-style links (the standard `[text](url "title")` format). The issue is in how the AST stack is being accessed when processing the title string - it's looking at the wrong position in the stack.

---
Repository: /testbed
