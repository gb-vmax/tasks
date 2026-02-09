# Bug Report

### Describe the bug

I'm encountering an issue with nested JSX tags in MDX files. When I have a self-closing tag inside another JSX component, I'm getting an error about an "Unexpected closing slash `/` in tag" even though the syntax appears to be valid.

### Reproduction

```jsx
<OuterComponent>
  <InnerComponent />
</OuterComponent>
```

When parsing the above MDX content, the parser throws an error claiming there's an unexpected closing slash, but the `<InnerComponent />` is a valid self-closing tag that should be allowed inside `<OuterComponent>`.

### Expected behavior

The parser should correctly handle self-closing JSX tags nested within other JSX components without throwing an error. This is standard JSX syntax and should be supported.

### Additional context

This seems to be related to how the parser tracks the tag stack when encountering the closing slash in self-closing tags. The error message suggests it's not recognizing that we're inside a parent tag when it encounters the `/` in the self-closing child tag.

---
Repository: /testbed
