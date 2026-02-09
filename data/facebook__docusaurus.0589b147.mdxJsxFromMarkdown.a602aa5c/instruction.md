# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag parsing where self-closing tags with a closing slash are throwing an error when they shouldn't be. The parser is incorrectly rejecting valid JSX syntax.

### Reproduction

```jsx
<MyComponent />
```

When trying to parse the above MDX content, I get an error:

```
Unexpected closing slash `/` in tag, expected an open tag first
```

This is valid JSX syntax and should be accepted. The self-closing tag format is standard in React/JSX and should work in MDX files.

### Expected behavior

Self-closing tags like `<MyComponent />` should parse without errors. The closing slash in a self-closing tag is not the same as a closing tag and shouldn't trigger validation errors about missing open tags.

### Additional context

This seems to have started happening recently. Previously, self-closing tags were working fine in my MDX files. Now any component using the self-closing syntax fails to parse.

---
Repository: /testbed
