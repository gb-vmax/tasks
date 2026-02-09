# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where lazy continuation lines in list items are being processed incorrectly. When I have a list item followed by an indented line that should be treated as a lazy continuation, the parser is handling it the opposite way - treating non-lazy lines as lazy and vice versa.

### Reproduction

```markdown
- List item
  This should be part of the list item (lazy continuation)
  
- Another item
    Indented content here
```

When parsing this markdown, the continuation lines that should be included in the list item are being rejected, and lines that shouldn't be part of lazy continuation are being accepted.

### Expected behavior

The parser should correctly identify lazy continuation lines and include them as part of the list item. Non-lazy continuation lines should be processed normally as part of the list content.

Currently it seems like the logic is inverted - lazy lines are being rejected when they should be accepted, and non-lazy lines are being accepted when they should follow the normal flow.

### System Info
- remark version: 15.0.1
- Browser: N/A (Node.js environment)

---
Repository: /testbed
