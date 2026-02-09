# Bug Report

### Describe the bug

I'm encountering an issue with object destructuring patterns in MDX code generation. When using object destructuring with multiple properties, the generated code appears to be malformed or produces unexpected output.

### Reproduction

```js
// Example MDX content with object destructuring
const MyComponent = ({ user, settings, theme }) => {
  return <div>{user.name}</div>
}

export default MyComponent
```

When this gets processed, the destructuring pattern doesn't seem to generate correctly. The properties appear to be accessed in the wrong order or with incorrect syntax.

### Expected behavior

Object destructuring patterns should be properly formatted in the generated output, with all properties correctly separated by commas and maintaining their original order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

Has anyone else run into this? It seems like the code generation for ObjectPattern might have an issue with how it iterates through properties.

---
Repository: /testbed
