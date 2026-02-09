# Bug Report

### Describe the bug

I'm experiencing an issue with markdown code fence parsing in Docusaurus. It seems like code blocks aren't being detected properly when there's content on the same line as the opening fence.

### Reproduction

When I have markdown content like this:

```markdown
```js console.log('hello')
some code here
```
```

The code fence detection appears to be inverted - it treats fences WITH content on the same line as closed, and fences WITHOUT content as open. This causes markdown links inside code blocks to be incorrectly processed.

### Expected behavior

Code fences should be properly identified as "definitely open" when there's content after the opening fence markers (like ` ```js some code`), and should NOT be marked as definitely open when it's just the fence markers alone (like ` ```js`).

This is affecting link replacement behavior inside code blocks - links that should be ignored are being processed, and vice versa.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
