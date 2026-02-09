# Bug Report

### Describe the bug

I'm experiencing an issue with directive text parsing where escaped colons in directives are not being handled correctly. When using a colon character (`:`) that should be escaped or treated as a character reference, the parser seems to be checking the wrong event in the event stack.

### Reproduction

```markdown
:directive[text with &#58; character reference]
```

When parsing directive text that contains a colon as a character reference (like `&#58;`), the parser incorrectly identifies it as a directive separator instead of treating it as part of the text content.

### Expected behavior

Character references containing colons (such as `&#58;`) should be properly recognized and not interfere with directive text parsing. The parser should check the correct event type to determine if a colon is part of a character reference.

### Additional context

This appears to be related to how the `previous` function validates whether a colon character should be treated as a directive delimiter. The function seems to be looking at the wrong position in the events array when checking for character references.

---
Repository: /testbed
