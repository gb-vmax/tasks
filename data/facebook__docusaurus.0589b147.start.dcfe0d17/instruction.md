# Bug Report

Title: Link title parsing broken when using parentheses

I've encountered an issue with parsing markdown links that have titles wrapped in parentheses. The parser seems to be incorrectly handling the closing marker for parentheses-style link titles.

Steps to reproduce:
1. Create a markdown link with a title using parentheses syntax: `[link](url "title")`
2. Try parsing links with different title delimiters (quotes vs parentheses)
3. The parentheses-style titles don't parse correctly

Example:
```markdown
[Example](https://example.com (This is a title))
```

Expected behavior:
The link title should be properly extracted and the closing parenthesis should match the opening one. Links with parentheses-wrapped titles should work the same way as those with quote-wrapped titles.

Current behavior:
The parser appears to be using the wrong closing marker for parentheses, causing the title parsing to fail or behave unexpectedly.

This seems to have started recently, possibly after some refactoring of the title parsing logic. The issue specifically affects the `factoryTitle` function when processing parentheses as title delimiters.

---
Repository: /testbed
