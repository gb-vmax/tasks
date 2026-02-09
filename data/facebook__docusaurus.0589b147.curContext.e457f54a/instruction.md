# Bug Report

### Describe the bug

I'm experiencing an issue with JSX parsing in MDX files. When using nested JSX elements with braces, the parser seems to be incorrectly determining the context of code blocks vs object literals. This causes valid JSX code to fail parsing or be interpreted incorrectly.

### Reproduction

```jsx
function MyComponent() {
  return (
    <div>
      {someCondition && {
        key: 'value'
      }}
    </div>
  )
}
```

When this type of nested structure is used, the parser appears to lose track of the proper context and treats braces in unexpected ways. The issue seems to affect how the parser distinguishes between block statements and object expressions within JSX.

### Expected behavior

The parser should correctly identify the context of braces and handle nested JSX structures with object literals properly. Valid JSX code should parse without errors.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be related to how the parser maintains its context stack when processing nested structures. Any help would be appreciated!

---
Repository: /testbed
