# Bug Report

### Describe the bug
Assets with explicit `fileName` set are being finalized even when they have no source content defined. This causes issues when trying to emit assets that have a filename but the source hasn't been set yet.

### Reproduction
```js
const assetId = this.emitFile({
  type: 'asset',
  fileName: 'my-asset.txt'
  // Note: source is not set yet
});

// Later trying to set the source fails because the asset
// was already finalized
this.setAssetSource(assetId, 'content');
```

### Expected behavior
Assets should only be finalized when they have source content available, regardless of whether a filename has been explicitly set. The presence of a filename alone shouldn't trigger finalization.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
