# Bug Report

### Describe the bug

I'm encountering an issue with string parsing where the opening quote character is being included in the parsed string output. This appears to be affecting string literals in the code.

### Reproduction

When parsing a string literal like:
```js
"hello world"
```

The parser is returning:
```
"hello world
```

Instead of the expected:
```
hello world
```

The opening quote character is incorrectly included in the final string value.

### Expected behavior

String literals should be parsed without including the surrounding quote characters. The parser should skip the opening quote before starting to collect the string content, and should properly handle the closing quote.

### Additional context

This seems to affect all string literals regardless of whether they use single or double quotes. The opening delimiter is consistently being included in the parsed result.

---
Repository: /testbed
