# Bug Report

### Describe the bug
I'm experiencing an issue with directive parsing where the leaf directive syntax is not being handled correctly. When I try to use a leaf directive with attributes, the parser seems to be applying the wrong logic for detecting the opening brace `{` character.

### Reproduction
```markdown
::leafDirective[label]{key="value"}
```

The directive should parse correctly with both the label and attributes, but it appears the condition for checking whether attributes are present is inverted. The parser is checking for `code !== 123` (not equal to `{`) instead of `code === 123` (equal to `{`), which causes it to attempt parsing attributes when it shouldn't and skip them when it should.

### Expected behavior
The parser should correctly identify when a `{` character is present after the label and attempt to parse attributes in that case. When no `{` is present, it should skip attribute parsing and move to the next step.

### System Info
- remark-directive version: 3.0.0
- Parser: micromark-based tokenizer

---
Repository: /testbed
