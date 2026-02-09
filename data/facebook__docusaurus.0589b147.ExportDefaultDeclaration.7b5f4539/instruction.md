# Bug Report

### Describe the bug

I'm experiencing an issue with export default declarations in MDX files. After a recent update, semicolons are being added incorrectly to export default statements, which is causing syntax errors in the generated code.

### Reproduction

When using an export default with a function declaration or class declaration in an MDX file:

```js
export default function MyComponent() {
  return <div>Hello</div>
}
```

The generated output incorrectly includes a semicolon after the function declaration:

```js
export default function MyComponent() {
  return <div>Hello</div>
};
```

This results in invalid JavaScript syntax.

### Expected behavior

Export default declarations with function/class declarations should NOT have a trailing semicolon, as this is not valid JavaScript syntax. Only export default with expressions (like object literals, arrow functions assigned to variables, etc.) should have semicolons.

For example:
- `export default function foo() {}` - no semicolon needed
- `export default class Bar {}` - no semicolon needed  
- `export default { key: value }` - semicolon needed

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
