# Bug Report

### Describe the bug

I'm experiencing an issue with the `wordsRegexp` function where it's not correctly handling multiple words. It seems like the regex pattern is only replacing the first space with a pipe character instead of all spaces, which causes the pattern matching to fail for keywords with multiple words.

### Reproduction

```js
// This should match any of the words separated by spaces
const pattern = wordsRegexp("foo bar baz");

// Expected to match "foo", "bar", or "baz"
console.log(pattern.test("foo")); // works
console.log(pattern.test("bar")); // doesn't work - should match but doesn't
console.log(pattern.test("baz")); // doesn't work - should match but doesn't
```

The generated regex pattern appears to be `^(?:foo|bar baz)` instead of `^(?:foo|bar|baz)$`, which only matches the first word correctly.

### Expected behavior

All words in the input string should be converted to alternation patterns in the regex, so each word can be matched independently. The function should replace all spaces with pipe characters to create proper alternation.

### System Info
- Version: latest
- Environment: Node.js

---
Repository: /testbed
