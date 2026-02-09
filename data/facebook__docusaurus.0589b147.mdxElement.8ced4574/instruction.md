# Bug Report

### Describe the bug

I'm experiencing an issue where MDX JSX elements are not being serialized correctly. The markdown output appears to be truncated or incomplete when converting MDX JSX nodes back to markdown format.

### Reproduction

When processing MDX content with JSX elements that have attributes, the serialization process seems to break midway through. This affects both flow and inline JSX elements.

```js
const mdxContent = `
<Component 
  prop1="value1"
  prop2="value2"
  prop3={expression}
>
  Content here
</Component>
`;

// After parsing and serializing back to markdown
// The output is incomplete/truncated
```

### Expected behavior

The JSX elements should be fully serialized back to markdown format with all attributes and content preserved. The output should be a complete, valid markdown representation of the original MDX content.

### Additional context

This seems to affect elements with multiple attributes, especially when they span multiple lines. The serialization appears to stop unexpectedly during the attribute processing phase.

---
Repository: /testbed
