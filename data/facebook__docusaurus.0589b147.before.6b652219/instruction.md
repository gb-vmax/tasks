# Bug Report

### Describe the bug

I'm encountering an issue with JSX flow tags in MDX content where the parser seems to be handling the tag incorrectly. After some recent changes, JSX components in flow context are not being parsed properly, causing the content to fail rendering or produce unexpected output.

### Reproduction

```mdx
<MyComponent prop="value">
  Some content here
</MyComponent>
```

When parsing the above MDX content with JSX flow tags, the component is not being recognized correctly. The issue appears to be related to how the parser processes opening and closing tags in flow context.

### Expected behavior

The JSX flow tag should be parsed correctly and the component should render with its content. The opening tag, attributes, and closing tag should all be properly identified and processed by the parser.

### Additional context

This seems to affect JSX components that are used at the block/flow level (not inline). The parsing behavior changed recently and now these components are not working as expected. Regular markdown content still works fine, but any JSX flow tags are problematic.

---
Repository: /testbed
