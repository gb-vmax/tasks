# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the content is being incorrectly processed. It seems like leading and trailing whitespace in code blocks is being stripped in an unexpected way, and the code block content might be getting attached to the wrong node in the AST.

### Reproduction

```mdx
# Example

```js
  function example() {
    return true;
  }
```

Some text after the code block.
```

When this MDX is processed, the code block's content doesn't appear correctly. The whitespace handling seems off - it's stripping more than just newlines at the start/end of the block.

### Expected behavior

The code block should preserve its internal formatting and whitespace correctly. Leading/trailing newlines should be removed, but internal indentation and spacing should remain intact. The code block value should also be assigned to the correct node in the syntax tree.

### Additional context

This appears to be related to how fenced code blocks are being parsed and processed. The issue manifests when using standard markdown code fences with language identifiers.

---
Repository: /testbed
