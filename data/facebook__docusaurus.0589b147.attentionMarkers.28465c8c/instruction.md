# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with attention markers (emphasis/strong) in MDX content. It seems like the parser is not correctly handling certain markdown emphasis syntax, possibly related to how attention markers are being processed.

### Reproduction

When trying to parse MDX content with emphasis markers, I'm getting unexpected behavior:

```js
const mdxContent = `
This is **bold text** and this is *italic text*.
`;

// The emphasis markers are not being recognized correctly
// Expected the text to be properly emphasized but it's not working
```

### Expected behavior

Emphasis markers like `*` and `**` should be properly recognized and processed to create italic and bold text respectively. The attention markers should be filtered and applied correctly to the content.

### Additional context

This seems to have started happening recently. The markdown emphasis syntax that used to work is now behaving differently. Not sure if this is related to how the constructs are being exported or if there's an issue with the marker filtering logic.

---
Repository: /testbed
