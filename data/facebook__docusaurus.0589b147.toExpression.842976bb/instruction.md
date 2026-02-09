# Bug Report

### Describe the bug

I'm encountering an issue with string replacement functionality after a recent update. When trying to replace strings in text content, the replacement doesn't work at all - the original string remains unchanged.

### Reproduction

```js
// Attempting to replace a simple string
const text = "Hello world, Hello everyone";
const result = replaceText(text, "Hello", "Hi");

// Expected: "Hi world, Hi everyone"
// Actual: "Hello world, Hello everyone" (no replacement occurs)
```

The replacement function seems to be completely broken. It's not replacing any occurrences of the search string, even though the input is a valid string.

### Expected behavior

When passing a string as the `find` parameter, all occurrences of that string should be replaced in the text. The function should create a proper regular expression with the global flag to match all instances.

### System Info
- Node version: 18.x
- Package version: latest

---
Repository: /testbed
