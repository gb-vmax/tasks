# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I include metadata after the language identifier in a code fence, the AST structure appears to be incorrect or missing expected nodes.

### Reproduction

```markdown
```javascript some-metadata
const x = 1;
```
```

When parsing this markdown, the metadata portion (`some-metadata`) doesn't seem to be properly wrapped in the expected node structure. The AST is missing the `codeFencedFenceMeta` node that should contain the metadata.

### Expected behavior

The parser should create a proper AST node hierarchy for code fence metadata, similar to how it handles the language identifier. The metadata should be wrapped in a `codeFencedFenceMeta` node containing the chunk string.

### Additional context

This affects any fenced code block that includes metadata after the language identifier. The metadata is still being processed but the node structure in the resulting AST is not what I would expect based on the markdown spec.

---
Repository: /testbed
