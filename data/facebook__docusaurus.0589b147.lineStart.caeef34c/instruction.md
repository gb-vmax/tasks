# Bug Report

### Describe the bug

I'm experiencing an issue with directive containers in my markdown parsing. When I have a directive container with content, the parser seems to be handling the content incorrectly - it's not processing the lines inside the container as expected.

### Reproduction

```markdown
:::note
This is some content
inside a directive container
:::
```

When parsing this markdown with remark-directive, the content inside the container doesn't get processed properly. It seems like the parser is ending the container prematurely or not recognizing the content lines correctly.

### Expected behavior

The directive container should properly parse all content between the opening `:::note` and closing `:::` fence, maintaining the text content and structure inside.

### Additional context

This appears to affect any directive container with multiple lines of content. Single-line containers or empty containers might work differently. The issue manifests when there's actual content that needs to be preserved within the directive boundaries.

---
Repository: /testbed
