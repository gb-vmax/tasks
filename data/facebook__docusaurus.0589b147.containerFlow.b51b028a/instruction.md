# Bug Report

### Describe the bug

I'm experiencing an issue with MDX rendering where the spacing between flow elements is incorrect. When I have multiple block-level elements (like paragraphs, headings, code blocks, etc.) in a container, the last two elements are being rendered without proper spacing between them.

### Reproduction

```mdx
# Heading

Some paragraph text.

Another paragraph.

Final paragraph.
```

When this gets rendered, the spacing between "Another paragraph" and "Final paragraph" is missing or incorrect, while the spacing between other elements appears normal.

### Expected behavior

All adjacent block-level elements should have consistent spacing (double newlines) between them. The last two elements should have the same spacing as all the other elements in the container.

### Additional context

This seems to affect any container flow content - I've noticed it with:
- Multiple paragraphs
- Headings followed by paragraphs
- Code blocks with surrounding content
- Lists with other elements

The issue appears to be specific to the last two elements in a container, as earlier elements render with correct spacing.

---
Repository: /testbed
