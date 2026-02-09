# Bug Report

### Describe the bug

I'm encountering an issue with directive attributes parsing in remark-directive. When processing directives with attributes, the attributes array seems to be getting initialized at the wrong time, causing attributes to not be properly captured or potentially causing undefined reference errors.

### Reproduction

```js
// Parse markdown with directive that has attributes
const markdown = ':directive[content]{#id .class key=value}';
const ast = processor.parse(markdown);

// The directive attributes are not being collected correctly
// Expected the attributes to be parsed and stored
// But they appear to be lost or undefined
```

### Expected behavior

Directive attributes should be properly initialized and collected during parsing. The attributes array should contain all the parsed attributes (id, classes, and key-value pairs) from the directive syntax.

### Additional context

This seems related to the order of operations when entering the attributes parsing state. The buffer initialization and attributes data structure setup might be happening in the wrong sequence, leading to attributes being lost or not properly accumulated.

---
Repository: /testbed
