# Bug Report

### Describe the bug

I'm encountering an issue with HTML attribute parsing in markdown content. When using attributes with underscores or hyphens in HTML tags within markdown, the parser seems to hang or behave unexpectedly.

### Reproduction

```markdown
<div data-test_value="example">content</div>
```

When processing markdown that contains HTML tags with attributes using underscores (like `data-test_value`), the parser doesn't handle them correctly. The same issue appears to affect attributes with hyphens and dots.

### Expected behavior

HTML attributes containing underscores, hyphens, dots, and colons should be parsed correctly without the parser getting stuck or failing to process the content.

### Additional context

This seems to affect inline HTML within markdown documents. Standard attributes work fine, but as soon as you introduce special characters like underscores in attribute names, things break down.

---
Repository: /testbed
