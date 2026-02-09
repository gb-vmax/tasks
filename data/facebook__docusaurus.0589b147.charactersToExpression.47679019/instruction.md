# Bug Report

### Describe the bug

I'm experiencing an issue with character escaping in regular expressions. When processing certain special characters, the escape pattern seems to be missing a character, which causes the regex to not match correctly.

### Reproduction

```js
// When trying to escape special characters for regex
const specialChars = ['.', '*', '+'];
const regex = charactersToExpression(specialChars);

// The dot character is not being properly escaped
const testString = 'test.example';
const result = testString.replace(regex, '');

// Expected: 'testexample' (dot should be matched and removed)
// Actual: 'test.example' (dot is not matched)
```

### Expected behavior

All special regex characters including the dot (`.`) should be properly escaped when building the expression. The resulting regex should match literal characters instead of treating them as regex metacharacters.

### Additional context

This appears to affect the `charactersToExpression` function in rehype-stringify. The dot character should be escaped in the replacement pattern but seems to be skipped, causing it to match any character instead of a literal dot.

---
Repository: /testbed
