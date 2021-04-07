# COVID-US: An Open-Source Open-Access Initiative

The COVID-19 pandemic continues to have a devastating effect on the health and well-being of the global population. Apart from the global health crises, the pandemic has also caused significant economic and financial difficulties and socio-physiological implications. Effective screening, prognosis, and treatment planning plays a key role in controlling the pandemic. A few recent studies highlighted the role of point-of-care ultrasound imaging for COVID-19 screening and prognosis, particularly given its non-invasive nature, widespread global accessibility and availability, and easy-to-sanitize nature.  Motivated by this and the promise of artificial intelligence tools to aid clinicians, we introduce __COVIDx-US__, an open-access benchmark dataset of COVID-19 related ultrasound imaging data that is the largest of its kind. The COVIDx-US dataset was curated from multiple sources and consists of __150__ lung ultrasound videos and __12,943__ processed images of patients with COVID-19 infection, non-COVID-19 infection, normal cases, as well as patients with other lung diseases/conditions. The dataset was systematically processed and validated specifically for the purpose of building and evaluating artificial intelligence algorithms and models. 

**Update 04/07/2021:** COVIDx-US v1.2 is released. We added 41 new ultrasound videos. The dataset now comprises 150 ultrasound videos and 12,493 processed ultrasound images. In addition, three labelling metadata files were released (located under the _labels_ folder) to ease up formulation of data science problems built on COVIDx-US to binary, 3-class, and 4-class classification problems.  
**Update 04/01/2021:** COVIDx-US v1.1 is released. We added 16 new ultrasound videos. The dataset now comprises 109 ultrasound videos and 11,307 processed ultrasound images.  
**Update 03/18/2021:** For a detailed description of the COVIDx-US dataset, please see our [paper](https://arxiv.org/abs/2103.10003).  
**Update 03/17/2021:** COVIDx-US v1.0 is released. The dataset comprises 93 ultrasound videos and 10,774 processed ultrasound images.

The current COVIDx-US dataset is constructed from the following open source datasets:
* [ButterflyNetwork](https://www.butterflynetwork.com/)
* [GrepMed](https://www.grepmed.com/)
* [The POCUS Atlas](https://www.thepocusatlas.com/)
* [LITFL](https://litfl.com/)   

# Licence
Our goal is to encourage broad adoption and contribution to this project. The COVID-US project is an open-source open-access initiative under the terms of the __GNU Affero General Public License 3.0__. Please review the LICENCE document for terms. Contact the team if you wish to licence COVID-US under different terms.

Conceptual flow of the data collection and processing flow
:-------------------------:
<img src="figure/Conceptual_flow.png" alt="COVID-US-Conceptual flow" width="100%" height="100%">


US video of a COVID-19 patient             |  Cropped video             |  First frame             |  First frame mask             |  Frame-67             |  Frame-67 mask
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="figure/6_butterfly_covid.gif"  alt="US video of a COVID-19 patient" width="100" height="172">  |  <img src="figure/6_butterfly_covid_cropped.gif" alt="cropped video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_cropped_convex_frame0.jpg" alt="first frame extracted from the video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_prc_convex_main_mask.jpg" alt="first frame mask" width="100" height="100">  |  <img src="figure/6_butterfly_covid_cropped_convex_frame67.jpg" alt="frame with moving pointer extracted from the video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_prc_convex_frame67_mask.jpg" alt="frame with moving pointer mask" width="100" height="100">


# Core COVID-US Team
1. National Research Council Canada
    * Ashkan Ebadi (ashkan.ebadi@nrc-cnrc.gc.ca)
    * Pengcheng Xi
    * Stephane Tremblay
2. Vision and Image Processing Research Group, University of Waterloo, Canada
    * Alexander Wong (alexander.wong@uwaterloo.ca)
    * Alexander MacLean

# Requirements
To generate the __COVIDx-US dataset__:
* Python >=3.6
* Pandas >=1.1.3
* BeautifulSoup
* selenium >=3.141.0
* requests >=2.24.0
* zipfile
* Jupyter

# How to Generate the COVIDx-US Dataset?
1. Use create_COVIDxUS.ipynb to extract the ultrasound videos from multiple sources and integrate them in the COVIDx-US dataset. 
    * __Note:__ Make sure to modify the file paths in the code to your own paths, if reuqired.

# COVIDx-US Data Distribution
Ultrasound __videos__ distribution per label and probe type

Class | Convex | Linear | Total
--- | --- | --- | ---
__COVID-19__ | 52 | 7 | `59`
__Pneumonia__ | 29 | 8 | `37`
__Normal__ | 7 | 6 | `13`
__Other__ | 24 | 17 | `41`



Ultrasound __videos__ distribution per label and data source

Class | ButterflyNetwork | PocusAtlas | GrepMed | LITFL | Total
--- | --- | --- | --- | --- | ---
__COVID-19__ | 33 | 18 | 8 | 0 | `59`
__Pneumonia__ | 0 | 9 | 9 | 19 | `37`
__Normal__ | 2 | 5 | 3 | 3 | `13`
__Other__ | 0 | 0 | 0 | 41 | `41`


# Citing this work
Please consider citing the following paper when using COVIDx-US dataset/scripts:

```
@article{COVIDxUS2021,
  title={COVIDx-US - An Open-Access Benchmark Dataset of Ultrasound Imaging Data for AI-Driven COVID-19 Analytics},
  author={Ebadi, Ashkan and Xi, Pengcheng and MacLean, Alexander and Tremblay, Stéphane and Kohli, Sonny and Wong, Alexander},
  journal={arXiv:2103.10003},
  year={2021}
}
```	

# Issues
After reading the README and past/current issues use the [issue tracker](https://github.com/nrc-cnrc/COVID-US/issues/) to report genuine bugs, mistakes or even small typos in the COVID-US project files. The tracker lets you browse and search all documented issues, comment on open issues, and track their progress. Note that issues are not meant for technical support; open an issue only for an error which is precise and reproducible.

# Contributing
You can contribute to the COVID-US initiative by providing/adding more data/data sources, implementing new features and functionalities in the scripts, correcting errors, or even improving documentation. Feel free to submit small corrections and contributions as issues in the [issue tracker](https://github.com/nrc-cnrc/COVID-US/issues/). For more extensive contributions, familiarize yourself with git and github, work on your own COVID-US fork and submit your changes via a [pull request](https://github.com/nrc-cnrc/COVID-US/pulls).

# Related work
* COVID-19 lung ultrasound [dataset](https://github.com/jannisborn/covid19_ultrasound/tree/master/data), link to the [paper](https://www.mdpi.com/2076-3417/11/2/672/html).
