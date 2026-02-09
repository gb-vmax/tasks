# Bug Report

### Describe the bug

Email autolinks are being incorrectly parsed and causing unexpected behavior. When the parser encounters text that should not be treated as an email autolink (due to failing validation checks), it's still proceeding with the tokenization instead of properly rejecting it.

### Reproduction

```js
// Text with invalid email patterns that should be rejected
const input = `
Some text with invalid@email patterns
that don't meet the criteria
`;

// The parser incorrectly processes these as autolinks
// even when validation fails
```

### Expected behavior

When the initial validation checks fail (invalid atext characters, previous character context, or unbalanced markers), the tokenizer should properly reject the input and not proceed with entering the "literalAutolink" and "literalAutolinkEmail" states.

Currently it seems like the validation runs but the parser continues processing as if the validation passed, leading to malformed AST nodes.

### System Info
- remark-gfm version: 4.0.0
- Parser encountering issues with email autolink detection

---
Repository: /testbed
