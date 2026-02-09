# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the label syntax is not being recognized correctly. When I try to use a directive container with a label (using square brackets), it seems like the parser is either skipping the label or not processing it as expected.

### Reproduction

```markdown
:::directive[label text]
content here
:::
```

When parsing the above markdown with a directive container that includes a label in square brackets, the label is not being handled properly. The parser appears to be checking for the wrong condition when determining whether to attempt parsing a label.

### Expected behavior

The parser should correctly detect and process labels enclosed in square brackets `[label]` that immediately follow the directive name. The label should be parsed and included in the resulting AST.

### Additional context

This seems to affect directive containers specifically - the logic for detecting when a label is present appears inverted. Instead of attempting to parse a label when square brackets are encountered (character code 91), it's doing the opposite.

---
Repository: /testbed
