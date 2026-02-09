# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer is not properly handling consumed state and callback order. When parsing certain MDX content, the parser appears to be calling callbacks in the wrong sequence and not correctly tracking whether tokens have been consumed.

### Reproduction

```js
// Parse MDX content with nested constructs
const mdx = `
# Heading

Some text with **bold** and _italic_.

\`\`\`js
code block
\`\`\`
`;

const result = compile(mdx);
// Parser callbacks are invoked in unexpected order
// Consumed state is not tracked correctly
```

### Expected behavior

The tokenizer should:
1. Correctly track the `consumed` state (should be `true` when a construct is successfully matched)
2. Call the `onreturn` callback with arguments in the correct order (`currentConstruct` first, then `info`)
3. Properly return to the previous state after processing

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to affect parsing of various MDX constructs where the tokenizer needs to backtrack or handle multiple possible matches.

---
Repository: /testbed
