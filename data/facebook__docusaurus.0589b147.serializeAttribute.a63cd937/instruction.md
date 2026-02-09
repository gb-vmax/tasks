# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute serialization where boolean attributes and empty string values are not being handled correctly. When I try to serialize HTML elements with boolean attributes (like `disabled`, `checked`, etc.), they're showing up in the output even when they should be omitted.

### Reproduction

```js
// Creating an element with a boolean attribute set to true
const element = {
  type: 'element',
  tagName: 'input',
  properties: {
    disabled: true,
    value: 'test'
  }
}

// Expected: <input disabled value="test">
// Actual: <input value="test"> (disabled is missing)
```

Also noticed that attributes with empty string values are being omitted when they shouldn't be:

```js
const element = {
  type: 'element',
  tagName: 'input',
  properties: {
    value: '',
    placeholder: 'Enter text'
  }
}

// Expected: <input value="" placeholder="Enter text">
// Actual: <input placeholder="Enter text"> (value is missing)
```

### Expected behavior

- Boolean attributes set to `true` should appear in the serialized output as the attribute name only (e.g., `disabled`)
- Attributes with empty string values should still be serialized with quotes (e.g., `value=""`)
- The quoting logic should properly determine when to use quotes vs when to omit them

This seems to have changed recently and is breaking my HTML generation. Any help would be appreciated!

---
Repository: /testbed
