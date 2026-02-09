# Bug Report

### Describe the bug

I'm encountering an issue with link titles in markdown parsing. When I use a link with a title attribute, the title seems to be getting assigned to the wrong node in the AST, causing unexpected behavior in the parsed output.

### Reproduction

```markdown
[example link](https://example.com "This is a title")
```

When parsing this markdown, the title `"This is a title"` appears to be associated with an incorrect node in the tree structure. The link renders but the title metadata is not being properly attached to the link node itself.

### Expected behavior

The title should be correctly assigned to the link node in the AST. When inspecting the parsed tree structure, the title property should belong to the same node as the URL.

### Additional context

This seems to affect any markdown link that includes a title attribute in quotes after the URL. Links without titles work fine, and the URL parsing itself appears correct - it's specifically the title assignment that's problematic.

---
Repository: /testbed
