# Bug Report

### Describe the bug

I'm encountering an issue with word matching in the MDX parser. It appears that words are being matched as prefixes instead of exact matches, causing incorrect behavior when parsing certain keywords or reserved words.

### Reproduction

When trying to parse MDX content with specific keywords, the parser is matching partial words instead of complete words. For example:

```js
// If we have a keyword list like "const let var"
// The parser should only match these exact words

// Currently this matches incorrectly:
"constant" // matches because it starts with "const"
"letter" // matches because it starts with "let"
"variable" // matches because it starts with "var"

// Expected: these should NOT match since they're not the exact keywords
```

This is causing false positives in keyword detection and breaking proper parsing of MDX content that contains words starting with reserved keywords.

### Expected behavior

The word matching should only match complete/exact words, not prefixes. Words like "constant", "letter", or "variable" should not be matched when looking for keywords "const", "let", or "var".

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
