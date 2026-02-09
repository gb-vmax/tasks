# Bug Report

### Describe the bug

HTML attributes with quoted values are not being parsed correctly in markdown. When using quoted attribute values in inline HTML tags, the parser seems to be terminating the quoted value prematurely or not recognizing the closing quote properly.

### Reproduction

```markdown
<div class="test-class">content</div>
<img src="image.jpg" alt="description" />
<a href="https://example.com" title="link title">text</a>
```

When parsing markdown with HTML tags that have quoted attributes, the attribute values are not being extracted correctly. The closing quote is not being matched properly, causing the parser to either consume the quote character incorrectly or fail to recognize the end of the attribute value.

### Expected behavior

The parser should correctly identify quoted attribute values, consume all characters within the quotes, and only terminate the quoted value when it encounters the matching closing quote character (either `"` or `'`).

For example:
- `class="test-class"` should parse the entire value `test-class`
- `title='link title'` should parse the entire value `link title`
- The closing quote should be consumed and the parser should move to the next state

### Additional context

This appears to affect any HTML tag with quoted attributes embedded in markdown content. The issue seems related to how the tokenizer handles the quote markers when processing attribute values.

---
Repository: /testbed
