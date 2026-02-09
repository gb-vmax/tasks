# Bug Report

### Describe the bug

I'm experiencing an issue with markdown to HTML conversion where the first child element is being skipped during processing. It seems like the parser is not correctly iterating through all child nodes in the tree.

### Reproduction

When converting markdown with multiple child elements, the first element gets lost:

```markdown
# Heading
First paragraph
Second paragraph
```

Expected output should include all three elements (heading + two paragraphs), but the first paragraph is missing from the converted HTML.

This appears to affect any parent node with multiple children - the first child is consistently skipped during the transformation process.

### Expected behavior

All child nodes should be processed and included in the output. The conversion should preserve all elements from the markdown source.

### Additional context

This seems to have started happening recently. The iteration logic might be off-by-one somewhere in the tree traversal code.

---
Repository: /testbed
