# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where attributes are being processed in the wrong order. When a directive has both a label and attributes, the parser seems to be handling them incorrectly, causing the directive syntax to not be recognized properly.

### Reproduction

```markdown
:directive[label]{attr="value"}
```

When parsing directives with this format (label followed by attributes), the parser doesn't process them correctly. It appears to skip the attributes section or process them out of order.

### Expected behavior

The parser should correctly handle directives with both labels and attributes in sequence. The label should be parsed first, followed by the attributes, and then the directive should complete successfully.

### Additional context

This seems to affect leaf directives specifically. The parsing flow appears to be jumping to the wrong state after processing the label portion of the directive.

---
Repository: /testbed
