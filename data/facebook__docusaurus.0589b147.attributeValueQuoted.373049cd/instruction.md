# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX content that contains JSX tags with quoted attribute values. When I have a tag with attributes like `<Component attr="value" />`, the parser seems to be consuming characters incorrectly and the content doesn't parse as expected.

### Reproduction

```jsx
// This MDX content fails to parse correctly
<MyComponent title="Hello World" />

// Also happens with single quotes
<MyComponent title='Hello World' />
```

The parser appears to be handling the quoted attribute values in the wrong order - it's exiting the value state before consuming all the characters, which leads to malformed parsing results.

### Expected behavior

The MDX parser should correctly handle JSX tags with quoted attribute values, consuming all characters within the quotes and properly recognizing the closing quote marker.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
