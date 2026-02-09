# Bug Report

### Describe the bug

When parsing MDX files with JSX tags, the tag name is not being set correctly. Instead of the tag name being assigned as a string, it seems like the wrong object is being referenced, which causes issues when trying to access or render the component.

### Reproduction

```jsx
// Example MDX content
<MyComponent />

<div>
  <CustomTag prop="value" />
</div>
```

When parsing the above MDX, the component names (`MyComponent`, `CustomTag`) are not extracted properly. This results in undefined or incorrect tag names in the parsed output.

### Expected behavior

The parser should correctly extract and store the primary tag name for JSX elements. The `tag.name` property should contain the string value of the tag name (e.g., "MyComponent", "CustomTag").

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have broken recently and is blocking our ability to parse MDX files correctly. Any help would be appreciated!

---
Repository: /testbed
