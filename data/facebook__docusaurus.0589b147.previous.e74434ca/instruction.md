# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing when using backticks. It seems like the parser is incorrectly handling backtick characters in certain contexts, particularly when there are character escapes involved.

### Reproduction

```js
// This doesn't parse correctly anymore
const text = '`code with \\` escape`'

// The backtick after the escape isn't being recognized properly
// Expected: inline code block
// Actual: parsing breaks or produces incorrect output
```

When I try to parse markdown with inline code that contains escaped backticks or has backticks in specific positions, the parser doesn't handle it as expected. The logic seems to have changed and now it's checking the wrong event position or using the wrong boolean operator.

### Expected behavior

Inline code blocks with backticks should be parsed correctly, especially when character escapes are present. The parser should properly identify when a backtick is part of the code content vs when it terminates the code block.

### System Info
- remark version: 15.0.1
- Node version: Latest

This might be related to how the tokenizer resolves code text boundaries. The behavior changed recently and is causing markdown with certain backtick patterns to fail parsing.

---
Repository: /testbed
