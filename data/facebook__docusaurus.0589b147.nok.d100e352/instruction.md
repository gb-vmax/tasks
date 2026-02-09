# Bug Report

### Describe the bug

I'm encountering an issue with the MDX tokenizer where it appears that state restoration is not being performed when a construct fails to match. This seems to cause the parser to continue from an incorrect position in the input stream, leading to parsing failures or incorrect output.

### Reproduction

```js
// When parsing MDX content with multiple potential constructs
const mdxContent = `
# Heading
Some text with **bold** and _italic_
`;

// The tokenizer fails to properly backtrack when a construct doesn't match
// This results in subsequent constructs being evaluated from the wrong position
```

### Expected behavior

When a construct fails to match (the `nok` callback is invoked), the tokenizer should restore the parser state to the position before attempting that construct. This allows the next construct in the list to be evaluated from the correct starting position.

Without proper state restoration, the parser position becomes inconsistent and can lead to:
- Incorrect parsing of valid MDX syntax
- Elements being skipped or misinterpreted
- Unexpected parser errors

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like it might be a regression since the state restoration logic appears to have been removed from the `nok` function in the tokenizer.

---
Repository: /testbed
