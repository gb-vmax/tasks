# Bug Report

### Describe the bug

HTML tag parsing is broken when there are spaces between the tag name and attributes. The parser seems to be consuming the closing `>` character incorrectly, causing HTML tags to not be recognized properly in markdown content.

### Reproduction

```markdown
<div class="test">content</div>
```

When parsing the above HTML in markdown, the tag is not being recognized correctly. It seems like the parser is looking for a `/` character (code 47) to close the tag, but it's actually encountering a `>` character (code 62) instead.

Also noticed that when there's whitespace before an attribute name, the parser transitions to the wrong state - it should stay in `tagOpenBetween` but instead moves to a different state.

### Expected behavior

HTML tags with attributes should be parsed correctly, with the parser properly handling:
- The closing `>` character to end the opening tag
- Whitespace between tag name and attributes
- Proper state transitions when processing tag content

### System Info
- Using remark version 15.0.1
- Issue appears in the HTML text tokenizer

---
Repository: /testbed
