# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag parsing where the closing behavior seems broken. When using JSX tags in MDX files, the parser appears to be handling the data exit incorrectly, which causes problems with the token processing.

### Reproduction

```mdx
<CustomComponent>
  Some content here
</CustomComponent>
```

When parsing MDX files with JSX tags like the above, the parser doesn't properly close/exit the data tokens. It looks like the exit callback is being replaced with another enter callback, so the data token never gets properly closed.

### Expected behavior

The parser should properly enter and exit data tokens when processing JSX tags in MDX. Both the enter and exit callbacks should be called with the correct token parameter.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to be affecting any MDX file that uses JSX components. The token buffer doesn't get properly flushed because the exit handler isn't being called correctly.

---
Repository: /testbed
