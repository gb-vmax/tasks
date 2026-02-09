# Bug Report

### JSX spread children syntax incorrectly transformed in preserve mode

I'm encountering an issue with JSX spread children when using `jsx: 'preserve'` mode. The spread operator (`...`) is being placed in the wrong position in the output.

### Reproduction

When bundling JSX code with spread children:

```jsx
<Component>
  {...items}
</Component>
```

With the following configuration:
```js
{
  jsx: 'preserve'
}
```

### Expected behavior

The JSX should be preserved as-is in the output:
```jsx
<Component>
  {...items}
</Component>
```

### Actual behavior

The spread operator appears to be moved to the end of the expression instead of the beginning, resulting in malformed JSX syntax in the output.

This seems to have broken after a recent change. The non-preserve modes appear to work fine, but preserve mode is producing invalid output.

---
Repository: /testbed
