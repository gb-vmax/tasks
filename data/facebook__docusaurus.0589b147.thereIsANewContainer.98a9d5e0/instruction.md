# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where nested container blocks aren't being properly closed before continuing with document parsing. This seems to affect how flow content (like code blocks, lists, etc.) is handled when transitioning between different container contexts.

### Reproduction

```mdx
> Blockquote with some content
> 
> ```js
> const code = 'block'
> ```
> 
> More content

Another paragraph
```

When parsing documents with nested containers (like blockquotes containing code blocks), the flow content doesn't get properly closed before exiting the container. This results in incorrect parsing of the document structure.

### Expected behavior

The parser should properly close any active flow content (like code blocks) before exiting container contexts and continuing with the rest of the document. The document structure should be correctly maintained when transitioning between nested containers.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
