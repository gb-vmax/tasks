# Bug Report

### Describe the bug

I'm encountering an issue with directive text parsing where attributes are not being processed correctly. When I use text directives with attributes in the format `:directive[label]{attr}`, the attributes section seems to be skipped or not parsed as expected.

### Reproduction

```markdown
:myDirective[some label]{key="value"}
```

When parsing this directive, the attributes `{key="value"}` are not being recognized or processed. The parser appears to be checking for the wrong condition when determining whether to attempt parsing attributes after the label.

### Expected behavior

The parser should properly detect and parse the attributes section (the part in curly braces) that comes after the label (the part in square brackets). Both the label and attributes should be available in the parsed output.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
