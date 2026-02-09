# Bug Report

### Describe the bug

JSX text content is not rendering at all in the output. Text nodes that should be visible are completely missing from the generated code.

### Reproduction

```jsx
const element = <div>Hello World</div>
```

After transpilation, the text "Hello World" is not included in the output. The div renders empty even though it contains text content.

This also affects more complex cases:

```jsx
const component = (
  <section>
    <h1>Title</h1>
    <p>Some paragraph text</p>
  </section>
)
```

All the text content ("Title" and "Some paragraph text") disappears from the output.

### Expected behavior

Text content within JSX elements should be preserved and rendered in the transpiled output. The text nodes should appear in the final code.

### Additional context

This seems to have started recently. Previously, JSX text was rendering correctly. Now any JSX with text content results in empty elements.

---
Repository: /testbed
