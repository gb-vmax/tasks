# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow elements inside containers. When I have JSX elements nested within other flow content (like lists or blockquotes), the indentation is being applied incorrectly. The JSX elements are getting indented when they shouldn't be, which breaks the output formatting.

### Reproduction

```jsx
<Container>
  <div>
    Content inside JSX element
  </div>
</Container>
```

When this JSX flow element is inside a parent container (like a list item or blockquote), the entire JSX block gets indented incorrectly. The indentation is being added to the JSX element itself rather than to the non-JSX content.

### Expected behavior

JSX flow elements should maintain their original formatting without additional indentation when nested inside container flow elements. Only regular markdown content should receive the container indentation.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
