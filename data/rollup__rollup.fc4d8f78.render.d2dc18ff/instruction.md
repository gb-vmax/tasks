# Bug Report

### Describe the bug

JSX spread attributes are being incorrectly transformed when using `jsx: 'preserve'` mode. The spread syntax `{...props}` is being removed/modified even though preserve mode should keep the JSX syntax intact.

### Reproduction

```jsx
// Input JSX with preserve mode enabled
const element = <Component {...props} />;

// Configuration
{
  jsx: 'preserve'
}
```

When compiling with `jsx: 'preserve'`, the spread attribute braces are being stripped out when they shouldn't be. The output is malformed instead of preserving the original JSX spread syntax.

### Expected behavior

With `jsx: 'preserve'` mode, the JSX spread attributes should remain unchanged in the output:
```jsx
<Component {...props} />
```

The preserve mode is supposed to keep JSX syntax as-is for further processing by other tools.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
