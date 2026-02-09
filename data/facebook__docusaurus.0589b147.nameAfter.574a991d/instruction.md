# Bug Report

### Describe the bug

I'm encountering an issue with directive attribute parsing where the initializer marker (`=`) is being consumed twice, causing the parser to fail or behave incorrectly when processing directive attributes.

### Reproduction

```js
// Using a directive with attributes like:
:::note{key=value}
Content here
:::

// Or inline directives:
:span{class=highlight}text:span
```

When parsing directives that have attributes with values (using the `=` sign), the parser appears to consume the equals sign but doesn't properly exit the attribute initializer type before moving to the value parsing stage.

### Expected behavior

The parser should correctly handle the attribute initializer marker by:
1. Entering the attribute initializer type
2. Consuming the `=` character
3. Exiting the attribute initializer type
4. Moving to value parsing

Instead, it seems like the exit is missing, which could lead to malformed AST nodes or parsing errors.

### Additional context

This appears to affect any directive syntax that uses key-value pairs in attributes. The issue is in the `nameAfter` function within the attributes factory.

---
Repository: /testbed
