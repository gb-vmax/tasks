# Bug Report

### Describe the bug
I'm encountering an issue with object parsing in MDX files. When I have object literals with multiple properties, the parser seems to hang or behave incorrectly. It looks like the parser is not properly terminating when it reaches the closing brace of an object.

### Reproduction
```js
const obj = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
}
```

When parsing MDX content that includes object literals like the above, the parser doesn't seem to recognize the end of the object properly. It appears to be looking for the wrong token to terminate the loop.

### Expected behavior
The parser should correctly parse object literals with multiple properties and properly recognize the closing brace `}` as the end of the object definition.

### Additional context
This seems to affect any object literal with more than one property in MDX files. Single-property objects might work, but multi-property objects cause parsing issues.

---
Repository: /testbed
