# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the order of operations seems incorrect when processing document flow. After some investigation, it appears that container exits are happening before chunk flow exits complete, which is causing unexpected behavior in the parsing state.

### Reproduction

When processing markdown documents with nested containers, the parser doesn't maintain the correct state between line continuations. This manifests as:

1. Parse a markdown document with nested block elements
2. The parser processes line endings
3. The continuation counter gets reset incorrectly
4. Subsequent lines are not parsed with the correct context

Example markdown that triggers the issue:
```markdown
> Blockquote line 1
> Blockquote line 2
```

The second line is not being recognized as part of the same blockquote context.

### Expected behavior

The parser should maintain proper state across line continuations. Container contexts should remain active until the chunk flow is properly exited, and the continuation counter should preserve its state correctly to handle multi-line block elements.

### Additional context

This seems to affect any markdown structure that spans multiple lines and requires maintaining parsing context. The issue appears to be related to how the flow continuation state is managed internally.

---
Repository: /testbed
