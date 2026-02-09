# Bug Report

### Describe the bug

I'm encountering an issue with markdown space parsing where the logic seems inverted. When processing markdown spaces, the parser is entering the wrong state based on whether a space character is detected or not.

### Reproduction

```js
// When parsing markdown with spaces
const input = "   text with leading spaces";

// The parser should:
// 1. Detect the space characters
// 2. Enter the space type
// 3. Process the prefix

// But instead it's doing the opposite - entering the space type 
// when there's NO space, and going to prefix when there IS a space
```

### Expected behavior

When `markdownSpace(code2)` returns true (indicating a space character is present), the parser should enter the type state and then proceed to the `prefix` function to consume the spaces. When there's no space, it should call `ok3` to continue with the next state.

Currently it seems backwards - it's calling `ok3` when a space is detected and `prefix` when no space is found.

### System Info
- Package: @mdx-js/mdx
- Version: 3.0.0

---
Repository: /testbed
