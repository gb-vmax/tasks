# Bug Report

### Describe the bug
When using self-closing JSX tags in MDX content, the parser is not properly handling the tag stack, which can lead to incorrect parsing behavior or errors when processing subsequent tags.

### Reproduction
```jsx
<Component />
<AnotherComponent>
  content here
</AnotherComponent>
```

After a self-closing tag, the parser seems to get confused about the tag stack state. This affects how subsequent opening and closing tags are validated and processed.

### Expected behavior
Self-closing tags should be properly handled and removed from the tag stack immediately after parsing, allowing subsequent tags to be processed correctly without any stack state issues.

### Additional context
This appears to be related to how the MDX parser manages the internal tag stack when encountering self-closing tags versus regular closing tags. The stack manipulation logic might not be accounting for all tag closure scenarios properly.

---
Repository: /testbed
