# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing in remark-directive. When using leaf directives (like `:directive-name`), the label syntax with square brackets `[label]` is not being parsed correctly. It seems like the parser is not properly detecting when a square bracket `[` should trigger label parsing.

### Reproduction

```markdown
:my-directive[some label]{.class}
```

When processing the above directive, the label `[some label]` should be recognized and parsed, but instead it appears to be skipped or handled incorrectly. The directive works fine without the label part:

```markdown
:my-directive{.class}
```

But adding the label causes unexpected behavior.

### Expected behavior

The parser should correctly identify the opening square bracket `[` (character code 91) and attempt to parse the label portion of the directive. Both forms should work:
- `:directive-name{attributes}` - without label
- `:directive-name[label]{attributes}` - with label

The label should be properly extracted and included in the resulting AST node.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
