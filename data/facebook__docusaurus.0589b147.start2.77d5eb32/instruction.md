# Bug Report

### Describe the bug

I'm experiencing an issue with JSX/MDX tag parsing where tags are not being properly recognized or processed. It seems like the tokenization is completing prematurely, causing tags to be malformed or not parsed at all.

### Reproduction

```jsx
<MyComponent>
  content here
</MyComponent>
```

When trying to parse MDX content with JSX tags, the tags don't seem to be getting tokenized correctly. The parser appears to be exiting the tag state too early before consuming the actual tag content.

### Expected behavior

JSX tags in MDX content should be fully parsed and tokenized, with the tag markers and content properly captured before the tokenizer exits the tag state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This might be related to recent changes in the tag factory function. The tokenization flow seems off compared to before.

---
Repository: /testbed
