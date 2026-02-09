# Bug Report

### Describe the bug

I'm experiencing an issue with markdown label parsing where the parser seems to get stuck in an infinite loop when processing label markers. The application becomes unresponsive when trying to parse certain markdown content with labels.

### Reproduction

```js
// Parsing markdown with labels causes the parser to hang
const markdown = '[some label]';
const result = remark().parse(markdown);
// Never completes - appears to be stuck in infinite recursion
```

### Expected behavior

The parser should successfully process the label syntax and return the parsed AST without hanging or entering an infinite loop.

### Additional context

This seems to affect markdown content that contains square bracket notation. The parser appears to enter an endless state transition and never exits. I noticed this started happening recently but I'm not sure what changed.

---
Repository: /testbed
