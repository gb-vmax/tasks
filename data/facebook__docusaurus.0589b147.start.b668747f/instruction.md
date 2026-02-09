# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where line endings in multi-line directives are not being handled correctly. The parser seems to get stuck in an infinite loop or fails to properly recognize line boundaries when processing directives that span multiple lines.

### Reproduction

```markdown
:::note
This is a multi-line
directive content
that should work
:::
```

When parsing the above directive, the tokenizer doesn't properly exit after consuming line endings, causing unexpected behavior in the parsing flow.

### Expected behavior

Multi-line directives should be parsed correctly with proper line ending recognition. Each line should be consumed and the parser should move to the next state appropriately.

### Additional context

This appears to be related to how the `tokenizeNonLazyLine` function handles state transitions. The line ending tokens seem to be processed but the parser doesn't advance to the correct next state.

---
Repository: /testbed
