# Bug Report

### Describe the bug
I'm encountering an issue with directive parsing in remark-directive where leaf directives with labels are not being parsed correctly. The parser seems to be checking for the wrong character code when processing directive names.

### Reproduction
```markdown
:directive-name[label text]{#id}
```

When trying to parse a leaf directive with a label (text in square brackets), the directive is not recognized properly. It appears the parser is looking for the closing bracket character (`]`, code 93) instead of the opening bracket character (`[`, code 91) after the directive name.

### Expected behavior
Leaf directives with labels should be parsed correctly:
- `:directive[label]` should work
- `:directive[label]{attrs}` should work
- The label content should be properly extracted

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems like it might be a regression or typo in the tokenizer logic. The character code check appears to be inverted.

---
Repository: /testbed
