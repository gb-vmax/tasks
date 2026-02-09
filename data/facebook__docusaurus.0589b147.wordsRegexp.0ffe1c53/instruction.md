# Bug Report

### Describe the bug

I'm encountering an issue with word boundary matching in regular expressions. It appears that certain words are being matched incorrectly when they appear as substrings within other words.

### Reproduction

```js
// When creating a regexp from a space-separated word list
const words = "if else return";
const regexp = wordsRegexp(words);

// This should NOT match, but it does
regexp.test("iffy");  // returns true (expected: false)
regexp.test("elsewhere");  // returns true (expected: false)

// These should match and do
regexp.test("if");  // returns true (correct)
regexp.test("else");  // returns true (correct)
```

### Expected behavior

The function should only match complete words, not partial matches within larger words. For example, "if" should match the word "if" but not match within "iffy" or "different".

### System Info
- Version: 3.0.0
- Node: 18.x

---
Repository: /testbed
