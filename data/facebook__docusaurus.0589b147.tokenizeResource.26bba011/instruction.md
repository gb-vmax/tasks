# Bug Report

### Describe the bug

Links with empty destinations are not being parsed correctly. When I have a markdown link with just `[text]()`, it's not being recognized as a valid link anymore.

### Reproduction

```js
const markdown = '[Click here]()';
const result = remark.parse(markdown);
// Expected: Should parse as a link node with empty destination
// Actual: Not parsing as a link at all
```

Also having issues with links that have parentheses in the title:

```js
const markdown = '[text](url "title (with parens)")';
const result = remark.parse(markdown);
// The title is not being parsed correctly
```

### Expected behavior

1. Links with empty destinations like `[text]()` should still be recognized as valid link syntax
2. Titles containing parentheses should be parsed correctly when properly quoted

This was working fine before and now my documentation with empty anchor links is broken.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
