# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where JSX components are not being recognized properly in MDX files. After a recent update, it seems like JSX syntax is being ignored or treated as plain text instead of being parsed as components.

### Reproduction

```mdx
import MyComponent from './MyComponent'

# Hello World

<MyComponent prop="value">
  Some content here
</MyComponent>
```

When parsing this MDX content, the `<MyComponent>` tags are not being processed correctly. They either get stripped out or rendered as plain text instead of being transformed into proper JSX elements.

### Expected behavior

The JSX components should be parsed and transformed correctly. The `<MyComponent>` should be recognized as a JSX element and included in the output AST with proper node types.

### Additional context

This seems to have started happening recently. MDX expressions (like `{variable}`) still work fine, but JSX components specifically are having issues. Import statements at the top of the file are being processed, but the actual component usage in the content is not.

---
Repository: /testbed
