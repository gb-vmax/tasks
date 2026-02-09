# Bug Report

### Describe the bug

I'm encountering an issue with MDX expression parsing where spread operators in JSX are being validated incorrectly. When I use a spread with a single property, I'm getting an error about "extra content in spread" even though there's only one property present.

### Reproduction

```jsx
<Component {...props} />
```

When parsing the above MDX content, the parser throws an error:
```
Unexpected extra content in spread: only a single spread is supported
```

This happens even though there's clearly only a single spread expression being used. The validation seems to be checking the wrong index in the properties array - it's checking if `properties[1]` exists when it should probably be checking `properties[0]` for the first property.

### Expected behavior

The parser should correctly validate that only a single spread is present and not throw an error when using a valid single spread expression like `{...props}`.

### Additional context

This seems to affect basic MDX usage with component props. The error is misleading because it suggests there's extra content when there isn't any.

---
Repository: /testbed
