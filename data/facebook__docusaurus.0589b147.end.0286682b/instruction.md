# Bug Report

### Describe the bug

I'm encountering an issue with directive leaf parsing where directives at the end of a file (without a trailing newline) are not being recognized properly. The parser seems to reject valid directive syntax when it appears as the last line of the document.

### Reproduction

```markdown
This is some text.

:directive[content]
```

When the above markdown is parsed without a trailing newline after the directive, it fails to be recognized as a valid directive. If I add a newline at the end of the file, it works as expected.

### Expected behavior

Directive leaf syntax should be valid regardless of whether it appears at the end of the file or has trailing content. The parser should accept directives followed by EOF (null character) just as it accepts directives followed by line endings.

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
