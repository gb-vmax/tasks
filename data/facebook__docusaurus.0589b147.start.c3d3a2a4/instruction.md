# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where line endings in non-lazy lines are not being processed correctly. The parser seems to get stuck in an infinite loop when handling certain directive syntax with multi-line content.

### Reproduction

```js
const directive = `
:::note
This is a multi-line
directive with content
spanning multiple lines
:::
`;

// Parser hangs or behaves unexpectedly when processing this
```

When trying to parse directives with content that spans multiple lines, the tokenizer doesn't advance properly through line endings. It appears to consume the line ending but then doesn't transition to the next state correctly.

### Expected behavior

The parser should correctly tokenize multi-line directive content, advancing through each line ending and continuing to process the content until the directive closes. Each line should be evaluated to determine if it's lazy or not, and the parser should move forward appropriately.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
