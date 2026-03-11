Hey, I need some help archiving some CI/CD pipeline configuration files for a deployment handoff. I have a set of pipeline configs stored under `/home/user/pipelines/` and I need to package them up into a compressed tarball that another team can drop into their environment.

Here's the situation: the `/home/user/pipelines/` directory contains several files, but I only want to archive the `.yml` files (not any other files like logs or notes). I need you to:

1. Create a gzip-compressed tar archive named `pipeline_configs.tar.gz` saved at `/home/user/artifacts/pipeline_configs.tar.gz`. The archive should contain only the `.yml` files from `/home/user/pipelines/`, and the files inside the archive should be stored with paths relative to `/home/user/pipelines/` — meaning when extracted, the `.yml` files should appear directly in the extraction directory (not inside a `pipelines/` subdirectory). For example, the file `/home/user/pipelines/build.yml` should be stored in the archive as `build.yml`, not as `pipelines/build.yml` or `/home/user/pipelines/build.yml`.

2. After creating the archive, verify its contents by listing all files inside `pipeline_configs.tar.gz` and writing that listing to `/home/user/artifacts/contents.txt`. The listing should contain one filename per line, with no leading `./` prefix and no extra metadata — just the bare filenames (e.g., `build.yml`, not `./build.yml` or `-rw-r--r-- user/user 0 2024-01-01 build.yml`). The filenames should be sorted alphabetically in `contents.txt`.

The `/home/user/artifacts/` directory does not exist yet — you'll need to create it.

To be clear about the expected result: after you're done, `/home/user/artifacts/contents.txt` should list exactly the `.yml` files that were archived, one per line, alphabetically sorted, with just the bare filename and no path prefix or extra whitespace.
