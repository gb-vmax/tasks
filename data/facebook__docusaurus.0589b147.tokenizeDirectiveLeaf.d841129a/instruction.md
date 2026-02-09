# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing in remark-directive. Leaf directives are not being recognized properly - they seem to require a semicolon (`;`) instead of a colon (`:`) to work, which breaks the standard directive syntax.

### Reproduction

```markdown
:directive-name[content]
```

The above directive syntax is not being parsed correctly. It appears the parser is expecting a semicolon instead of the standard colon character.

Additionally, directives at the end of lines or before line breaks are not being handled properly - they seem to require both a null character AND a line ending to be recognized, when they should work with either condition.

### Expected behavior

1. Leaf directives should use the standard `:` (colon) syntax as specified in the directive specification
2. Directives should be properly recognized when followed by either a line ending OR at the end of input (null character)

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This appears to be a regression as the standard directive syntax was working in previous versions.

---
Repository: /testbed
