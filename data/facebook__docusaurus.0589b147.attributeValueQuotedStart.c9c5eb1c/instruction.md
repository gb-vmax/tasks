# Bug Report

### Describe the bug

I'm encountering an issue with quoted attribute values in JSX/MDX tags. When I use attributes with quoted values, the parser seems to be closing the attribute value prematurely or incorrectly handling the closing quote marker.

### Reproduction

```jsx
<Component name="value" />
```

When parsing the above JSX, the attribute value handling appears broken. The parser doesn't correctly recognize when the closing quote matches the opening quote.

### Expected behavior

The parser should properly match opening and closing quotes for attribute values. An attribute like `name="value"` should:
1. Recognize the opening quote `"`
2. Parse the content `value`
3. Recognize the matching closing quote `"`
4. Move on to the next attribute or close the tag

Currently, it seems like the condition for detecting the closing quote marker is inverted or incorrect, causing the parser to exit the attribute value state at the wrong time.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
