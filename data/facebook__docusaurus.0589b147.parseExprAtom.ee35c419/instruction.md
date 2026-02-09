# Bug Report

### Describe the bug

I'm encountering an issue with JSX parsing where JSX tags are being incorrectly parsed as text elements. It seems like the parser is confusing JSX opening tags with text content, causing unexpected behavior when rendering JSX components.

### Reproduction

```jsx
const Component = () => {
  return (
    <div>
      <span>Hello</span>
    </div>
  )
}
```

When parsing this JSX, the `<span>` tag is being treated as text instead of being recognized as a JSX element. This results in the component not rendering correctly.

### Expected behavior

JSX tags should be properly identified and parsed as elements, not as text content. The parser should distinguish between `jsxTagStart` tokens and `jsxText` tokens correctly.

### Additional context

This appears to be related to how the parser handles different token types in the `parseExprAtom` method. The issue manifests when nested JSX elements are present in the component tree.

---
Repository: /testbed
