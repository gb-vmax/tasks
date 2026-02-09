# Bug Report

### Describe the bug

I'm experiencing an issue with rendering nested container flow elements in markdown. When processing documents with multiple children in a container, the last child element appears to be processed twice, and there seems to be an off-by-one error in the iteration logic.

### Reproduction

```js
const markdown = `
- Item 1
- Item 2
- Item 3
`;

const processor = remark();
const result = processor.processSync(markdown);
```

When processing a list or other container with multiple children, the iteration goes one step beyond the actual array length, causing the last element to be handled incorrectly. This leads to duplicate processing or undefined behavior.

### Expected behavior

Each child element in a container should be processed exactly once, and the iteration should stop at the last valid index (children.length - 1). The indexStack should also be initialized correctly to track the current position accurately.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
