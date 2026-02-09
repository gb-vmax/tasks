# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where restoring tokenizer state doesn't properly handle the stack. When the parser backtracks during tokenization (for example, when trying different parsing strategies), the internal stack state appears to be getting corrupted or shared between different parsing attempts.

### Reproduction

This happens when parsing complex markdown structures that require the tokenizer to try multiple parsing strategies. For example:

```markdown
- List item with **bold text**
  - Nested item
```

When the parser encounters ambiguous syntax that requires backtracking, subsequent parsing operations seem to be affected by leftover state from previous attempts. The issue manifests as:

1. Parser tries one interpretation of the markdown
2. Backtracks when that doesn't work
3. Tries an alternative interpretation
4. The stack from step 1 somehow interferes with step 3

### Expected behavior

When the tokenizer backtracks and restores a previous state, the internal stack should be completely independent from the current state. Each parsing attempt should start with a clean slate based on the saved checkpoint, without any cross-contamination between attempts.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems like it might be related to how JavaScript handles object references, but I'm not entirely sure. The parser works fine for simple cases but fails on more complex nested structures that trigger backtracking.

---
Repository: /testbed
