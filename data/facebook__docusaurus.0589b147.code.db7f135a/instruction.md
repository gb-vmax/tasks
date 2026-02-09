# Bug Report

### Describe the bug

I'm experiencing an issue with code fence rendering in markdown. When I have code blocks that contain backticks in the content, the output fence markers are not using enough backticks to properly escape the content.

### Reproduction

```js
const markdown = `
\`\`\`
This code contains ``` backticks
\`\`\`
`;

// Process this markdown
const result = remark().stringify(parse(markdown));
console.log(result);
```

The output fence should use at least 4 backticks (or more) to properly wrap content that contains 3 backticks, but it seems to be using fewer backticks than needed.

### Expected behavior

When code blocks contain backtick sequences, the fence markers should use MORE backticks than the longest sequence found in the content. For example, if the content has ``` (3 backticks), the fence should use at least ```` (4 backticks) to properly escape it.

Currently getting malformed output where the fence doesn't properly wrap the content.

### Additional context

This seems to affect any code block where the content includes backtick sequences. The fence generation logic might not be calculating the correct number of backticks needed.

---
Repository: /testbed
