# Bug Report

### Describe the bug

I'm encountering an issue with keyword matching in MDX parsing. It seems like certain reserved words or keywords are not being recognized properly, which causes the parser to fail or incorrectly parse valid MDX content.

### Reproduction

```js
// When using specific keywords in MDX content
const mdxContent = `
export function MyComponent() {
  return <div>Hello</div>
}
`;

// The parser fails to recognize 'export' and 'function' as valid keywords
// and treats them as regular text instead
```

### Expected behavior

Keywords like `export`, `function`, `import`, etc. should be properly recognized and parsed as JavaScript/JSX syntax within MDX files. The regex pattern should match these keywords at word boundaries.

### Additional context

This appears to be related to how the keyword matching regex is constructed. The pattern doesn't seem to be anchoring properly to match complete words, which might cause it to match partial strings or fail to match valid keywords altogether.

---
Repository: /testbed
