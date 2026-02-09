# Bug Report

### Describe the bug

When using JSX with `jsx: 'preserve'` mode, the curly braces around JSX expressions are being incorrectly removed during the build process. The output should keep the original JSX syntax intact when preserve mode is enabled, but instead the braces are stripped out.

### Reproduction

```js
// Input JSX file
const element = <div>{someVariable}</div>;
const component = <Component prop={value} />;
```

With rollup config:
```js
{
  jsx: 'preserve'
}
```

Expected output (preserve mode):
```js
const element = <div>{someVariable}</div>;
const component = <Component prop={value} />;
```

Actual output:
```js
const element = <div>someVariable</div>;
const component = <Component propvalue />;
```

### Expected behavior

When `jsx: 'preserve'` is set, the JSX syntax including expression containers (curly braces) should be preserved as-is in the output. The braces should only be removed when using transform modes like `jsx: 'automatic'` or `jsx: 'classic'`.

### Additional context

This seems to have broken the preserve mode functionality. The curly braces are essential for distinguishing between string literals and expressions in JSX, so removing them corrupts the output when preserve mode is intended to keep the original JSX syntax.

---
Repository: /testbed
