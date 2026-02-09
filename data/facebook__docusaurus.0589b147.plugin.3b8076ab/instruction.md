# Bug Report

### Describe the bug

I'm experiencing an issue with heading ID parsing in MDX files. When using custom heading IDs with the `{#id}` syntax, the ID is being extracted from the wrong position in the heading node tree, causing text to be incorrectly removed or corrupted.

### Reproduction

```md
## My Heading *with emphasis* and text {#custom-id}
```

When this heading is processed, the text content gets mangled. It seems like the parser is looking at the wrong child node when trying to extract and remove the custom ID portion.

### Expected behavior

The heading should be properly parsed with:
- Text: "My Heading *with emphasis* and text"
- ID: "custom-id"

The emphasis formatting should remain intact and all text before the `{#custom-id}` should be preserved correctly.

### Additional context

This appears to affect headings that have multiple child nodes (like when using bold/italic syntax or other inline formatting). Simple headings without formatting seem to work fine, but as soon as you have nested nodes in the heading, the ID extraction logic targets the wrong node.

---
Repository: /testbed
