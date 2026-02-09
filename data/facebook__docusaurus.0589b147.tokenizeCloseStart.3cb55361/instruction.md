# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence is not being recognized properly when it has leading whitespace. The code block doesn't close as expected and continues to consume subsequent content as part of the code block.

### Reproduction

```mdx
# Example

    ```js
    const x = 1;
    ```

More content here
```

When the closing fence has indentation/leading spaces, it's not properly matched with the opening fence. The "More content here" text gets treated as part of the code block instead of being parsed as regular markdown content.

### Expected behavior

Code blocks with indented closing fences should close properly when the fence sequence matches or exceeds the opening fence length, regardless of leading whitespace. The closing fence should be recognized and subsequent content should be parsed normally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Previously indented closing fences were handled correctly.

---
Repository: /testbed
