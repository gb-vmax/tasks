I need help archiving some Kubernetes operator manifests before I do a cluster upgrade. I have a directory at `/home/user/k8s/operators` that contains manifest files for several operators we've deployed. I want to create a compressed backup archive of all the YAML files in that directory tree.

Here's what I need you to do:

1. Create a gzip-compressed tar archive of **all `.yaml` files** found anywhere under `/home/user/k8s/operators`, saving it to `/home/user/backups/manifests_backup.tar.gz`. The paths stored inside the archive should be **relative** (not absolute) — they should start with `operators/` not `/home/user/k8s/operators/`. To get the relative paths, you should run tar from the `/home/user/k8s` directory.

2. After creating the archive, write a verification file at `/home/user/backups/manifests_backup.txt` that lists the contents of the archive (one file path per line, exactly as stored inside the archive). This should be a plain listing of the archived file paths — no permissions, no timestamps, no sizes, just paths. The lines should be in the same order that `tar -tf` outputs them.

The `/home/user/backups` directory may not exist yet — make sure it gets created.

The final `/home/user/backups/manifests_backup.txt` file should look something like:
```
operators/cert-manager/cert-manager.yaml
operators/cert-manager/webhook.yaml
...
```
(but with the actual files that are present, in the order tar lists them)

Please make sure the `.tar.gz` file is a valid gzip-compressed archive that can be extracted with `tar -xzf`.
