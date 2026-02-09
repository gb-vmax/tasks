# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where nested content isn't being serialized correctly. When parsing markdown with nested structures (like lists, blockquotes, or other containers), the output seems to be malformed or incomplete.

### Reproduction

```js
const processor = remark();

const markdown = `
> This is a blockquote
> with multiple lines
`;

const result = processor.processSync(markdown);
console.log(result.toString());
```

When processing markdown with nested elements, the serialized output doesn't match the expected structure. It appears that the content is being converted incorrectly, possibly using the entire stack instead of just the popped element.

### Expected behavior

The markdown should be parsed and serialized back to a properly formatted string that matches the input structure. Nested elements should maintain their hierarchy and format correctly.

### Additional context

This seems to affect any markdown with nested structures - blockquotes, lists, code blocks, etc. The output is not what I'd expect from the remark processor.

---
Repository: /testbed
