# Bug Report

### Describe the bug

I'm encountering an issue with parsing directive text that contains attributes. When a directive has curly braces `{` for attributes, the parser doesn't handle them correctly and the directive fails to parse as expected.

### Reproduction

```markdown
:directive[label]{attr="value"}
```

When parsing the above directive text, the attributes section (the part in curly braces) is not being processed properly. The parser seems to be checking for the wrong condition when determining whether to attempt parsing attributes.

### Expected behavior

The directive should correctly parse both the label and attributes sections. Directives with the format `:name[label]{attributes}` should be fully recognized and the attributes should be accessible in the parsed output.

### Additional context

This affects inline directives (directive text) that use the standard syntax with square brackets for labels and curly braces for attributes. The issue appears to be in the tokenization logic when transitioning from the label to the attributes section.

---
Repository: /testbed
