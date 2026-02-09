# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing in remark-directive. When using container directives with labels, the parser seems to be handling the label syntax incorrectly. Specifically, directives that should accept labels are not being parsed properly.

### Reproduction

```markdown
:::note[This is a label]
Some content here
:::
```

When parsing this directive, the label `[This is a label]` is not being recognized or processed correctly. The parser appears to be taking the wrong code path when encountering the opening bracket `[` character.

### Expected behavior

The parser should correctly identify and process the label portion of the container directive. The label should be parsed as part of the directive structure and made available in the resulting AST.

### Additional context

This seems to affect container directives specifically. The issue appears to be in the tokenization logic where the parser decides whether to attempt parsing a label based on the character code.

---
Repository: /testbed
