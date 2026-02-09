# Bug Report

### Describe the bug

I'm encountering an issue with nested JSX tags in MDX files. When I have multiple levels of nested components, the parser incorrectly throws an error about unexpected closing slashes even though the tags are properly nested.

### Reproduction

```jsx
<Outer>
  <Inner>
    <Deepest />
  </Inner>
</Outer>
```

When parsing MDX content with nested self-closing or closing tags at deeper nesting levels, I get an error message:
```
Unexpected closing slash `/` in tag, expected an open tag first
```

This happens even though the tags are correctly structured and properly nested. The error seems to trigger when there are 2 or more levels of nesting.

### Expected behavior

The parser should correctly handle nested JSX tags at any depth without throwing errors about unexpected closing slashes. Properly nested and closed tags should parse successfully.

### Additional context

This appears to be related to how the tag stack is being validated. The issue only manifests with deeper nesting levels - single level nesting works fine.

---
Repository: /testbed
