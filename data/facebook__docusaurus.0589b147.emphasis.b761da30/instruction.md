# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis (italic) text rendering in markdown processing. When I use emphasis syntax in my markdown, the output appears to be broken or empty. It seems like the emphasis handler is not correctly processing the node's children.

### Reproduction

```js
const markdown = `This is *emphasized text* in a sentence.`;
// Process the markdown through remark-rehype

// Expected: <p>This is <em>emphasized text</em> in a sentence.</p>
// Actual: The emphasized portion is missing or malformed
```

Another example:
```markdown
Here is some *italic text* that should work.

Multiple *emphasis* blocks *should* work too.
```

The emphasized portions either don't render at all or render incorrectly.

### Expected behavior

Emphasis markers (`*text*` or `_text_`) should be properly converted to `<em>` tags with the correct content inside them.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
