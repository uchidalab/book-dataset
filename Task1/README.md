# Book Dataset - Task 1

[Top](/../../)

[Results](/../../docs/results.md)

## Task 1: Classification

### A. Book Cover Image to Genre (BookCover30)

This task is to explore the entire book database. There are 137,788 books in 32 classes. This dataset contains book cover images, title, author, and subcategories for each respective book.

#### File Structure

>book30-listing-train.csv
>book30-listing-test.csv

Training set and test set with all attributes including image URL, title, author, and category.

Format:
```
"[AMAZON INDEX (ASIN)}","[FILENAME]","[IMAGE URL]","[TITLE]","[AUTHOR]","[CATEGORY ID]","[CATEGORY]"
```

Example:
```
"1588345297","1588345297.jpg","http://ecx.images-amazon.com/images/I/51l6XIoa3rL.jpg","With Schwarzkopf: Life Lessons of The Bear","Gus Lee","1","Biographies & Memoirs"
"1404803335","1404803335.jpg","http://ecx.images-amazon.com/images/I/51UJnL3Tx6L.jpg","Magnets: Pulling Together, Pushing Apart (Amazing Science)","Natalie M. Rosinsky","4","Children's Books"
```

>bookcover30-labels-train.txt
>bookcover30-labels-test.txt

Simplified training set and test set ground truth listed by image name and class number (listed below).

Format:
```
[FILENAME] [CLASS NO.]
```

Example:
```
1588345297.jpg 1
1404803335.jpg 4
```

#### Category ID

30 classes

Training - 51,300 Total

Test - 5,700 Total

|Label|Category Name|Training Size|Test Size|
|---|---|---|---|
|0|Arts & Photography|1,710|190|
|1|Biographies & Memoirs|1,710|190|
|2|Business & Money|1,710|190|
|3|Calendars|1,710|190|
|4|Children's Books|1,710|190|
|5|Comics & Graphic Novels|1,710|190|
|6|Computers & Technology|1,710|190|
|7|Cookbooks, Food & Wine|1,710|190|
|8|Crafts, Hobbies & Home|1,710|190|
|9|Christian Books & Bibles|1,710|190|
|10|Engineering & Transportation|1,710|190|
|11|Health, Fitness & Dieting|1,710|190|
|12|History|1,710|190|
|13|Humor & Entertainment|1,710|190|
|14|Law|1,710|190|
|15|Literature & Fiction|1,710|190|
|16|Medical Books|1,710|190|
|17|Mystery, Thriller & Suspense|1,710|190|
|18|Parenting & Relationships|1,710|190|
|19|Politics & Social Sciences|1,710|190|
|20|Reference|1,710|190|
|21|Religion & Spirituality|1,710|190|
|22|Romance|1,710|190|
|23|Science & Math|1,710|190|
|24|Science Fiction & Fantasy|1,710|190|
|25|Self-Help|1,710|190|
|26|Sports & Outdoors|1,710|190|
|27|Teen & Young Adult|1,710|190|
|28|Test Preparation|1,710|190|
|29|Travel|1,710|190|
