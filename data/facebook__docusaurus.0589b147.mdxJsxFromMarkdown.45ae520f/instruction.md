# Bug Report

### Describe the bug

I'm encountering an issue with closing tags in MDX JSX parsing. When I have a self-closing tag or closing tag in my MDX content, the parser seems to be calling `exit` at the wrong time, which causes the tag stack to get out of sync.

### Reproduction

```mdx
<MyComponent>
  Some content
</MyComponent>
```

When parsing this structure, the closing tag handling appears to be broken. The parser exits the token before popping from the stack, which means the state gets corrupted.

### Expected behavior

The parser should properly handle opening and closing JSX tags in MDX content. The tag stack should be maintained correctly throughout parsing, with items being popped off the stack before exiting tokens.

### Additional context

This seems to affect any MDX content with closing tags. The issue appears to be in the `mdxJsxFromMarkdown` function where closing tags are processed. The order of operations for handling the tag stack and exiting tokens doesn't seem right.

---
Repository: /testbed
