# Bug Report

### Describe the bug

HTML attribute values in markdown are being parsed incorrectly. When parsing HTML tags with quoted attribute values, the parser seems to be consuming characters in the wrong order or transitioning to the wrong state, which causes the attribute value parsing to fail or behave unexpectedly.

### Reproduction

```markdown
<div class="test">content</div>
```

When this markdown is processed, the HTML tag's quoted attribute value doesn't parse correctly. The parser appears to be moving to the wrong state after consuming characters within the quoted value.

### Expected behavior

HTML tags with quoted attributes should be parsed correctly, with the attribute value properly recognized and the parser transitioning through the correct states as it processes the opening quote, value content, and closing quote.

### Additional context

This seems to affect any HTML tag in markdown that uses quoted attribute values (both single and double quotes). The issue appears to be in the state machine logic that handles the quoted attribute value parsing.

---
Repository: /testbed
