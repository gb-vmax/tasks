# Bug Report

### Describe the bug
I'm encountering an issue with markdown parsing where code blocks and other non-lazy continuation content is being handled incorrectly. It seems like the parser is treating lazy continuation lines as non-lazy and vice versa, causing content that should be included in blocks to be excluded or improperly parsed.

### Reproduction
```js
const markdown = `
> quote line 1
> 
>     code block inside quote
>     second line of code
`;

// Parse this markdown
const result = remark.parse(markdown);

// The code block lines are not being properly recognized
// They're being treated as if they're lazy continuation when they shouldn't be
```

### Expected behavior
Code blocks and other non-lazy content within block quotes should be properly parsed and included in the AST. The parser should correctly distinguish between lazy continuation lines (which can omit the `>` marker) and non-lazy content (which requires explicit markers).

Specifically:
- Lines that are genuinely non-lazy continuations should be parsed as part of the containing block
- Lines that fail the non-lazy test should be rejected appropriately
- The logic for checking null/end-of-input conditions should work correctly

### System Info
- remark version: 15.0.1
- Node version: 18.x

This appears to have started happening recently and is affecting markdown documents with nested block structures.

---
Repository: /testbed
