# Bug Report

### Describe the bug

I'm experiencing an issue with JSX rendering where empty expressions and whitespace-only text nodes are being treated incorrectly. When a JSX element contains empty expressions (`{/* */}` or `{}`) or text nodes that should be ignored, they're still being included in the output with commas, resulting in malformed JSX output.

### Reproduction

```jsx
// Example 1: Empty expression
const element = <div>
  Hello
  {}
  World
</div>

// Example 2: Whitespace-only text
const element2 = <div>
  <span>Item 1</span>
  
  <span>Item 2</span>
</div>
```

After bundling, these elements have extra commas in unexpected places where the empty expressions or whitespace nodes were removed.

### Expected behavior

Empty JSX expressions and whitespace-only text nodes should be completely removed without leaving any artifacts (like extra commas) in the rendered output. The output should be clean and properly formatted.

### Additional context

This seems to affect JSX elements with multiple children where some children are empty or whitespace-only. The issue manifests as extra commas appearing in the compiled output where these nodes were stripped out.

---
Repository: /testbed
