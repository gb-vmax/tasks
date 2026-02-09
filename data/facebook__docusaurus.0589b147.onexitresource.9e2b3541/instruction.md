# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with reference handling in MDX compilation. When processing documents with multiple references (links/images), the compiler seems to lose track of data after the first reference is processed, causing subsequent references to fail or behave incorrectly.

### Reproduction

```mdx
Here's a [link](https://example.com) and another [link](https://example.org).

![image](https://example.com/img.png)

More content with [references](https://test.com).
```

When compiling MDX content with multiple references like the above, only the first reference processes correctly. Subsequent references in the same document don't work as expected - they either throw errors or get rendered incorrectly.

### Expected behavior

All references (links and images) in an MDX document should be processed independently and correctly, regardless of how many references appear in the document. Each reference should maintain its own context without interfering with others.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening in the latest version. Previously, multiple references in the same document worked fine.

---
Repository: /testbed
