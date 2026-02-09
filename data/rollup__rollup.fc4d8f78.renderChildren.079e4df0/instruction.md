# Bug Report

### Describe the bug

When using JSX with multiple children elements, the comma separator is being inserted at the wrong position in the rendered output. The comma appears after the child content instead of before it, causing syntax errors in the generated code.

### Reproduction

```jsx
const element = (
  <div>
    <span>First</span>
    <span>Second</span>
  </div>
);
```

After compilation, the children are rendered with commas in incorrect positions, leading to malformed JavaScript output.

### Expected behavior

The comma separators between JSX children should be placed before each child element (after the previous child's end position), not after the current child's content. The generated code should be valid JavaScript with properly positioned argument separators.

### Additional context

This seems to affect any JSX element with multiple children. Single-child elements work fine, but as soon as there are two or more children, the comma placement becomes incorrect.

---
Repository: /testbed
