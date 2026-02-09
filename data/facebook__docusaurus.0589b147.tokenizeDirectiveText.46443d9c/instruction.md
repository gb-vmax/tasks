# Bug Report

### Describe the bug

I'm encountering an issue with inline directive parsing where the tokenizer is not correctly handling certain character codes. Specifically, directives with colons (`:`) in certain positions are being rejected when they should be accepted, and the opening brace check appears to be using the wrong character code.

### Reproduction

```markdown
:directive[label]{attributes}
```

When parsing inline directives in the format above, the parser is incorrectly handling the character validation. The directive should be properly tokenized but instead fails at unexpected points during parsing.

### Expected behavior

The inline directive syntax should be properly tokenized and parsed. Directives with the standard format `:name[label]{attributes}` should work correctly without being rejected during the tokenization phase.

### Additional context

This seems to affect the `tokenizeDirectiveText` function in the remark-directive parser. The character code checks for determining valid tokens appear to be inverted or using incorrect values, causing valid directive syntax to fail parsing.

---
Repository: /testbed
