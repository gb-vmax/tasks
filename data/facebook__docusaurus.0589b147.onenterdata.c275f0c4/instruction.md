# Bug Report

### Describe the bug

I'm encountering an issue where text nodes in markdown are not being properly created when they should be. It seems like the logic for checking whether to create a new text node has been inverted or broken.

### Reproduction

When parsing markdown content that should result in text nodes being created, the parser is failing because it's trying to push `undefined` to the stack instead of a properly initialized text node.

For example, parsing simple markdown like:

```markdown
Hello world
```

Should create text nodes properly, but instead the parser appears to be skipping text node creation in certain cases where a new text node should be initialized.

### Expected behavior

The parser should:
1. Check if the last sibling exists and is not a text node
2. If no sibling exists OR the last sibling is not a text node, create a new text node
3. Push the text node to both the siblings array and the stack

Currently it seems like text nodes are only being created when a sibling exists AND is not a text node, which misses the case where no siblings exist at all.

### Additional context

This appears to be related to the `onenterdata` function in the compiler. The condition for creating new text nodes may have been changed incorrectly.

---
Repository: /testbed
