# Bug Report

### Describe the bug

HTML closing tags in markdown are not being parsed correctly. It seems like tags with alphanumeric characters in the closing tag name are not recognized properly, causing the parser to fail or behave unexpectedly.

### Reproduction

```markdown
<div>content</div>
<span>text</span>
<custom-tag>data</custom-tag>
```

When parsing the above markdown with HTML tags, the closing tags don't get tokenized correctly. This affects any HTML element with alphanumeric characters in the tag name.

### Expected behavior

The parser should correctly recognize and tokenize HTML closing tags that contain alphanumeric characters (letters and numbers). Both standard HTML tags like `</div>`, `</span>` and custom tags like `</custom-tag>` should be parsed without issues.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
