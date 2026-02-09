# Bug Report

### Describe the bug

I'm experiencing an issue with parsing directives that contain closing brackets `]` in their labels. When a directive label contains a single closing bracket without a matching opening bracket, the parser fails to properly recognize the end of the label.

### Reproduction

```markdown
:directive[text with ] bracket]
```

When parsing the above directive, the label should be `text with ] bracket`, but the parser seems to be treating the first `]` as the end of the label instead of continuing until it finds the unmatched closing bracket.

### Expected behavior

The parser should correctly handle unmatched closing brackets within directive labels. A closing bracket should only terminate the label when it doesn't have a corresponding opening bracket (i.e., when the bracket balance reaches zero).

For example:
- `:directive[text with ] bracket]` should parse with label: `text with ] bracket`
- `:directive[text [nested] here]` should parse with label: `text [nested] here`

### Additional context

This appears to be related to the bracket balancing logic in the label parsing. The issue manifests when there's an unmatched closing bracket that should be part of the content rather than marking the end of the label.

---
Repository: /testbed
