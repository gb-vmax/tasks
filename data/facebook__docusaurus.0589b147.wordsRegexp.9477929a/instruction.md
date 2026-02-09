# Bug Report

### Describe the bug

I'm experiencing an issue with word matching in MDX content. It seems like the word boundary detection is not working as expected - words are being matched even when they appear as part of larger words or substrings.

### Reproduction

When processing MDX content with specific keywords, the matching behavior is incorrect:

```js
// Expected: only match exact words "foo" or "bar"
// Actual: matches "foo" within "foobar", "bar" within "sidebar", etc.

const keywords = "foo bar";
// Processing content with these keywords incorrectly matches partial words
```

For example, if I have keywords like "const let var", it's matching these even when they appear inside other words like "constant" or "letter", which shouldn't happen.

### Expected behavior

The word matching should only match complete words, not partial matches within larger strings. If the keyword is "bar", it should match " bar " but not "sidebar" or "foobar".

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
