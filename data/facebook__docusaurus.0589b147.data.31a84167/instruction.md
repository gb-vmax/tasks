# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When using backticks to create inline code spans, the parser seems to be handling the backtick character (`` ` ``) incorrectly within the code content itself.

### Reproduction

When parsing markdown with inline code that contains backticks, the output is not what I expect:

```markdown
This is `code with a ` backtick` inside
```

The parser appears to be treating the backtick differently than it should. The inline code span should be properly delimited, but instead it seems like the internal backtick is causing unexpected behavior.

### Expected behavior

Inline code spans should properly handle backticks within the code content according to the CommonMark spec. The parser should correctly identify where code spans begin and end, even when backticks appear in the data portion.

### Additional context

This seems related to how the tokenizer processes characters within code text sequences. The issue manifests when the character code 96 (backtick) appears in certain positions during parsing.

---
Repository: /testbed
