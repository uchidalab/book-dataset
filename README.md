# Book Cover Dataset

This dataset contains 207,572 books from the Amazon.com, Inc. marketplace.

## Challenges

[Results and related papers](docs/results.md)

### Task 1: Classification

#### A. Book Cover Image to Genre (BookCover30)

The purpose of this task is to classify the books by the cover image. The BookCover30 dataset contains 57,000 book cover images divided into 30 classes. The training set and test set is split into 90% - 10% respectively.

[Technical details](./Task1)

### Task 2: Data Mining

#### Data Mining (Book32)

This task is to explore the entire book database. There are 207,572 books in 32 classes. This dataset contains book cover images, title, author, and category for each respective book.

[Technical details](./Task2)

## Use

### Full Images

Due to size constraints, the full images aren't available in this repository. However, we provide label files with URLs to the images hosted on Amazon. Note, the fidelity of the images cannot be guarenteed. A script to download them can be found in [scripts](./scripts).

### (224 x 224 x 3) Images

Resized images for the BookCover30 dataset are available in this download.

[Download](https://drive.google.com/a/human.ait.kyushu-u.ac.jp/file/d/1LVWYXn2WdF-7NuLbl_LyyEwXSvIJUdPr/view?usp=sharing) (657 MB)

## Citation

[Paper on arXiv](https://arxiv.org/abs/1610.09204)

B. K. Iwana, S. T. Raza Rizvi, S. Ahmed, A. Dengel, and S. Uchida, "Judging a Book by its Cover," *arXiv preprint arXiv:1610.09204 (2016)*.

```
@article{iwana2016judging,
  title={Judging a Book by its Cover},
  author={Iwana, Brian Kenji and Raza Rizvi, Syed Tahseen and Ahmed, Sheraz and Dengel, Andreas and Uchida, Seiichi},
  journal={arXiv preprint arXiv:1610.09204},
  year={2016}
}
```

## Contact

brian@human.ait.kyushu-u.ac.jp

## Disclaimer

All book cover images are hosted by and copyright Amazon.com, Inc. The the use of the book cover images is fair use for academic purposes.
