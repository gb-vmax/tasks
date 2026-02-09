# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where certain code blocks or inline code elements are not being tokenized correctly. The parser seems to be skipping or mishandling specific character codes, leading to unexpected parsing behavior.

### Reproduction

When processing MDX content with specific character patterns, the tokenizer appears to incorrectly evaluate null code points. This results in constructs not being properly recognized or applied.

Example MDX content that triggers the issue:
```mdx
# Test Document

Some text with `inline code` here.

```js
const example = null;
```

More content follows.
```

The parser processes this content but doesn't apply the correct constructs in certain scenarios, particularly when dealing with null values or specific character boundaries.

### Expected behavior

The tokenizer should correctly identify and apply construct definitions for all valid code points, including proper handling of null checks. All inline code and code blocks should be parsed and rendered correctly regardless of the character codes encountered.

### Additional context

This seems to be related to how the tokenizer maps code points to construct definitions. The logic for determining which constructs to apply appears to have some edge cases that aren't handled properly.

---
Repository: /testbed
