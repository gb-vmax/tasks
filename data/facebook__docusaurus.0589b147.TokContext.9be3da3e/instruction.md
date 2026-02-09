# Bug Report

### Describe the bug

I'm experiencing strange parsing behavior with MDX content after a recent update. It seems like whitespace handling and code generation context are getting mixed up in the tokenizer. The parser is treating expression contexts incorrectly, which causes unexpected output when processing MDX files.

### Reproduction

When parsing MDX content with mixed expressions and static content, the tokenizer appears to be applying the wrong context rules. For example:

```mdx
Some text {expression} more text

<Component>
  {codeBlock}
</Component>
```

The whitespace preservation and override behavior don't match what's expected based on the token context. Expression contexts seem to be bleeding into places where they shouldn't, and the generator flag is being applied incorrectly.

### Expected behavior

The tokenizer should:
- Preserve whitespace only when the `preserveSpace` flag is set for that specific context
- Apply the correct `override` behavior based on the token type, not other unrelated flags
- Keep expression contexts separate from generator contexts

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be affecting how the parser handles the internal token context state, leading to incorrect parsing decisions downstream.

---
Repository: /testbed
