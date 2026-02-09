# Bug Report

### Describe the bug

I'm encountering an issue with image syntax parsing where the footnote support check seems to be inverted. When using image syntax like `![alt](url)` in markdown content, the parser is behaving unexpectedly when footnote constructs are present.

### Reproduction

```js
// When _hiddenFootnoteSupport is defined in parser constructs
const parser = {
  constructs: {
    _hiddenFootnoteSupport: true
  }
}

// Parsing image syntax: ![example](image.png)
// The parser incorrectly rejects valid image syntax when it should accept it
```

The issue appears to be related to how the parser handles the label marker for images when checking for footnote support. Valid image syntax gets rejected in contexts where it should be accepted.

### Expected behavior

Image syntax should be parsed correctly regardless of whether `_hiddenFootnoteSupport` is present in the parser constructs. The parser should accept valid `![...]` image labels properly.

### System Info
- remark version: 15.0.1
- Browser/Node: Any

---
Repository: /testbed
