# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where list items are not being properly processed. When parsing MDX content that contains lists, the last list item seems to be getting cut off or not included in the output.

### Reproduction

```js
const mdx = `
- First item
- Second item
- Third item
`;

const result = compile(mdx);
// Only two items are returned instead of three
```

The issue appears to be related to how the compiler iterates through events when processing lists. The last item in a list doesn't get included in the final output.

### Expected behavior

All list items should be included in the parsed output. If there are three items in the source MDX, all three should appear in the compiled result.

### Additional context

This seems to have started happening recently. I noticed that lists that previously worked correctly are now missing their final items. The issue is consistent across different types of lists (ordered and unordered).

---
Repository: /testbed
