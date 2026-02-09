# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where labels are not being processed correctly. It seems like the parser is skipping or mishandling the first character after the opening bracket in directive labels.

### Reproduction

When using directives with labels, the parsing behavior is incorrect:

```markdown
::directive[label text]{#id}
```

The label content doesn't parse as expected - it appears the parser state machine isn't properly transitioning after consuming the opening bracket marker.

### Expected behavior

The directive label should be parsed correctly with all characters included. The parser should properly handle the transition from the opening marker to the label content.

### Additional context

This appears to affect all directive types (text, leaf, and container directives) that use label syntax. The issue manifests when the parser processes the opening `[` character and should begin reading the label content.

---
Repository: /testbed
