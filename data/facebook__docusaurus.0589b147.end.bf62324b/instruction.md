# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where closing braces `}` in directive attributes are not being handled correctly. The parser seems to be rejecting valid directive syntax that should be accepted.

### Reproduction

```markdown
:directive{key="value"}
```

When parsing directives with attributes, the closing brace should properly close the attribute block and continue parsing. However, it appears that valid directive syntax with attributes is being incorrectly rejected.

### Expected behavior

Directives with properly formatted attributes should be parsed successfully. The closing `}` should mark the end of the attributes block and allow the directive to be processed normally.

### Additional context

This affects any directive that uses the attribute syntax with curly braces. The parser should recognize the closing brace as a valid terminator for the attributes section.

---
Repository: /testbed
