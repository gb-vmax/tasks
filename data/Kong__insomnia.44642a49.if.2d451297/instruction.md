# Bug Report

### Describe the bug

I'm encountering an issue where object properties with underscores are not being rendered correctly. It seems like properties that start with an underscore are being skipped or handled differently than expected.

### Reproduction

```js
const data = {
  _privateField: 'should be rendered',
  normalField: 'works fine'
}

const result = await render(data);
// _privateField is not processed as expected
```

When I have an object with properties starting with underscore (like `_id`, `_private`, etc.), they don't get rendered properly. Regular properties without the underscore prefix work fine.

### Expected behavior

Properties starting with underscore should be rendered the same way as other properties. The underscore prefix shouldn't affect the rendering behavior.

### Additional context

This seems to have started recently. I'm using objects with `_id` fields from my database and they're not being processed correctly anymore.

---
Repository: /testbed
