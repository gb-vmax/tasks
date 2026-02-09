# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content rendering where whitespace handling seems broken. When I have code blocks or content with tabs/spaces, the output is getting mangled - extra spaces are appearing where they shouldn't be, or spaces are missing entirely.

### Reproduction

```jsx
// Example MDX content that's not rendering correctly
const MyComponent = () => {
  return (
    <div>
      {/* Content with tabs gets weird spacing */}
      <pre>
        Code here
          Indented line
      </pre>
    </div>
  )
}
```

The rendered output has incorrect whitespace - sometimes adding spaces where there shouldn't be any, or removing spaces that should be there. This affects code formatting and makes the output look really messy.

### Expected behavior

Whitespace should be preserved correctly, especially in code blocks and pre-formatted text. Tabs and spaces should render as expected without being added or removed unexpectedly.

### Additional context

This seems to have started happening recently. The MDX parser appears to be processing chunks incorrectly, possibly related to how it handles tab characters and space conversion. The serialization logic might be off by one or inverting some condition.

---
Repository: /testbed
