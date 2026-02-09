# Bug Report

### Describe the bug

I'm encountering an issue with HTML attribute serialization where attributes with certain values are not being properly encoded/escaped. It appears that attribute values are being rendered directly without going through the entity encoding process.

### Reproduction

```js
const element = {
  type: 'element',
  tagName: 'div',
  properties: {
    title: 'Hello "World"'
  }
}

// The output includes unescaped quotes in the attribute value
// Expected: <div title="Hello &quot;World&quot;"></div>
// Actual: <div title="Hello "World""></div>
```

When serializing HTML elements with attribute values that contain special characters (like quotes), the output is not properly escaped. This breaks the HTML structure and can cause parsing issues.

### Expected behavior

Attribute values should be properly encoded with character entities when they contain special characters. Quotes inside attribute values should be converted to their entity equivalents (`&quot;` or `&#x22;`).

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
