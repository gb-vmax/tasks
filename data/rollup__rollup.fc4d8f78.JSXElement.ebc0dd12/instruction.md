# Bug Report

### Describe the bug

When using JSX with spread attributes followed by regular attributes in automatic mode, the props object structure is getting corrupted. The attributes that come after a spread are not being properly wrapped in an object, causing them to be treated as separate arguments instead of being merged into the props.

### Reproduction

```jsx
// This JSX code:
const element = <Component {...spreadProps} regularProp="value" />;

// Gets transformed incorrectly, resulting in invalid output
// The regularProp is not properly merged into the props object
```

Another example that fails:

```jsx
<div {...spread} className="test" id="example" />
```

The attributes after the spread operator aren't being correctly handled - they should be merged into the props object but instead appear to be rendered as separate parameters.

### Expected behavior

Attributes that appear after a spread attribute should be properly wrapped in an object and merged with the spread props. The transformation should produce valid code where all props are correctly combined.

### System Info
- JSX mode: automatic
- Using spread attributes with additional props

---
Repository: /testbed
