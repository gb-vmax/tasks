# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where colons (`:`) in text directives are not being handled correctly. It seems like the parser is failing to properly recognize when a colon should be treated as part of the directive syntax versus when it should be escaped.

### Reproduction

```markdown
:directive[text with \: escaped colon]
```

When parsing directives that contain escaped colons, the behavior is incorrect. The parser appears to be checking the wrong event in the event stack when determining if a colon character is escaped or not.

### Expected behavior

The parser should correctly distinguish between:
- Escaped colons (`\:`) which should be treated as literal colon characters
- Unescaped colons (`:`) which are part of the directive syntax

The logic for checking whether a previous character is escaped should look at the correct position in the events array.

### System Info
- remark-directive version: 3.0.0
- Parser encountering issues with character escape detection

---
Repository: /testbed
