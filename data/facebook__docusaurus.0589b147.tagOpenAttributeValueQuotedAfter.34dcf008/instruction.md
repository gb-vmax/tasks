# Bug Report

### Describe the bug

HTML tags with attributes are not being parsed correctly in markdown. When an HTML tag has quoted attribute values followed by other attributes or the closing `>`, the parser fails to recognize the tag properly.

### Reproduction

```markdown
<div class="test" id="example">content</div>
```

or

```markdown
<span title="hello" data-value="world">text</span>
```

When parsing these HTML tags in markdown content, the parser doesn't handle the transition from quoted attribute values to the next part of the tag correctly. Tags with a single attribute seem to work fine, but multiple attributes or certain attribute patterns cause issues.

### Expected behavior

HTML tags with multiple quoted attributes should be parsed correctly, just like they are in standard HTML. The parser should properly recognize:
- Quoted attribute values (both single and double quotes)
- Multiple attributes in sequence
- The closing `>` after quoted attributes
- Self-closing tags with attributes like `<img src="test.jpg" />`

### System Info
- Version: Latest
- Browser: N/A (parser issue)

---
Repository: /testbed
