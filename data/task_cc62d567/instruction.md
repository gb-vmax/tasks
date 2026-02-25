You are a research assistant helping to organize image datasets for a machine learning experiment. 

1. In the directory /home/user/data, there are several subdirectories: /home/user/data/raw_images, /home/user/data/old, and /home/user/data/temp. In /home/user/data/raw_images/, each JPEG image filename starts with a prefix identifying the dataset (e.g., "cats_123.jpg", "dogs_456.jpg", "birds_789.jpg"). 

2. Your goal is to create the following folder structure inside /home/user/data/organized: 
   - /home/user/data/organized/cats
   - /home/user/data/organized/dogs
   - /home/user/data/organized/birds

3. Move all images with filenames starting with "cats_" to /home/user/data/organized/cats, those with "dogs_" to /home/user/data/organized/dogs, and those with "birds_" to /home/user/data/organized/birds. Do not move any other images.

4. Move the entire /home/user/data/old folder (and all its contents) to a new directory named /home/user/data/archive.

5. Delete the /home/user/data/temp directory and all of its contents.

6. After all operations, generate a summary file named /home/user/data/organization_log.txt with the following format (exactly, to enable automated verification):

---
Datasets Organized: <num_cats> cats images, <num_dogs> dogs images, <num_birds> birds images
Old files archived to: /home/user/data/archive/old
Temporary files deleted: /home/user/data/temp
Directories created under /home/user/data/organized:
- cats
- dogs
- birds
---

<num_cats>, <num_dogs>, and <num_birds> should be replaced with the actual number of images moved to each category.

Ensure the structure and content of organization_log.txt is exactly as above, with "Datasets Organized" summary, archive confirmation, deleted folder, and directory listing (one per line after the hyphen).
