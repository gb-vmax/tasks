# Bug Report

### Describe the bug

I'm experiencing an issue with JSX flow tags in MDX content. When using JSX components in flow (block-level) context, the parser seems to be incorrectly handling the closing of tags. The behavior appears inconsistent - sometimes tags are parsed correctly, other times they're not recognized properly.

### Reproduction

```mdx
<MyComponent>
  Some content here
</MyComponent>

<AnotherComponent />
```

When parsing the above MDX content, the JSX flow tags don't seem to be processed correctly. The parser appears to be looking for the wrong character code when determining how to handle the tag closure.

### Expected behavior

JSX flow tags (block-level JSX components) should be parsed correctly regardless of whether they're self-closing or have separate opening/closing tags. The parser should properly recognize the `>` character that closes the opening tag.

### Additional context

This seems to affect both self-closing tags and tags with separate closing elements. The issue manifests when the parser tries to determine what comes after a JSX flow tag - it doesn't seem to be checking for the correct character to proceed with parsing.

---
Repository: /testbed
