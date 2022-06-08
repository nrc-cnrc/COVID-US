# COVIDx-US: An open-access benchmark dataset of COVID-19 related ultrasound imaging

The COVID-19 pandemic continues to have a devastating effect on the health and well-being of the global population. Apart from the global health crises, the pandemic has also caused significant economic and financial difficulties and socio-physiological implications. Effective screening, prognosis, and treatment planning plays a key role in controlling the pandemic. A few recent studies highlighted the role of point-of-care ultrasound imaging for COVID-19 screening and prognosis, particularly given its non-invasive nature, widespread global accessibility and availability, and easy-to-sanitize nature.  Motivated by this and the promise of artificial intelligence tools to aid clinicians, and as part of a large open-source initiative, __[the COVID-Net initiative](https://alexswong.github.io/COVID-Net/)__, we introduce __COVIDx-US__, an open-access benchmark dataset of COVID-19 related ultrasound imaging data that is the largest of its kind. The COVIDx-US dataset was curated from multiple sources and consists of __242__ lung ultrasound videos and __29,651__ processed images of patients with COVID-19 infection, non-COVID-19 infection, normal cases, as well as patients with other lung diseases/conditions. It also contains a standardized and unified lung ultrasound score per video file, providing better interpretation while enabling other research avenues such as severity assessment. The dataset was systematically processed and validated specifically for the purpose of building and evaluating artificial intelligence algorithms and models. 

**Update 05/30/2022:** COVIDx-US v1.5 is released. The dataset now contains a unified and standardized human "gold standard" lung ultrasound score __(LUSS)__ per video file!  
**Update 07/13/2021:** COVIDx-US v1.4 is released. We added three new data sources. The dataset now comprises 242 ultrasound videos and 29,651 processed ultrasound images.  
**Update 04/29/2021:** COVIDx-US v1.3 is released. We added two new data sources (Radiopaedia and CoreUltrasound). The dataset now comprises 173 ultrasound videos and 16,822 processed ultrasound images.  
**Update 04/12/2021:** Data dictionary added. This [excel file](https://github.com/nrc-cnrc/COVID-US/blob/main/utils/Data%20Dictionary.xlsx) contains detailed information about the variables/features in the metadata files.  
**Update 04/07/2021:** COVIDx-US v1.2 is released. We added 41 new ultrasound videos. The dataset now comprises 150 ultrasound videos and 12,493 processed ultrasound images. In addition, three labelling metadata files were released (located under the _labels_ folder) to ease up formulation of data science problems built on COVIDx-US to binary, 3-class, and 4-class classification problems.  
**Update 04/01/2021:** COVIDx-US v1.1 is released. We added 16 new ultrasound videos. The dataset now comprises 109 ultrasound videos and 11,307 processed ultrasound images.  
**Update 03/18/2021:** For a detailed description of the COVIDx-US dataset, please see our [paper](https://arxiv.org/abs/2103.10003).  
**Update 03/17/2021:** COVIDx-US v1.0 is released. The dataset comprises 93 ultrasound videos and 10,774 processed ultrasound images.

The current COVIDx-US dataset is constructed from the following datasets:
* [ButterflyNetwork](https://www.butterflynetwork.com/)
* [GrepMed](https://www.grepmed.com/)
* [The POCUS Atlas](https://www.thepocusatlas.com/)
* [LITFL](https://litfl.com/)
* [Radiopaedia](https://radiopaedia.org/)
* [CoreUltrasound](https://www.coreultrasound.com/)   
* University of Florida   
* Scientific publications   
* [Clarius](https://clarius.com/)   

# License
### COVIDx-US license
Our goal is to encourage broad adoption and contribution to this project. The COVID-US project is an open-source open-access initiative under the terms of the __GNU Affero General Public License 3.0__. Please review the LICENCE document for terms. Contact the team if you wish to licence COVID-US under different terms.

### Data sources license
* Data sources with Creative Commons (CC) license:
	* __The POCUS Atlas__ - [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
	* __LITFL__ - [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
	* __Radiopaedia__ - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) 

* Data sources without license information (no data usage license is mentioned on their websites):
	* __ButterflyNetwork__
	* __GrepMed__
	* __CoreUltrasound__
	* __Clarius__

__Notes__
1. The above data sources are all public sources. 
2. We do not host any data on the COVIDx-US repository.
3. Users have the responsibility to verify with the unlicensed data sources to see if their intended usage is allowed. We take no responsibility for any data use by users.
4. For the licensed data sources, it's users' responsibility to verify if their usage is allowed according to the license.

# Conceptual flow
Conceptual flow of the data collection and processing
:-------------------------:
<img src="figure/Conceptual_flow.png" alt="COVID-US-Conceptual flow" width="100%" height="100%">


US video of a COVID-19 patient             |  Cropped video             |  First frame             |  First frame mask             |  Frame-67             |  Frame-67 mask
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="figure/6_butterfly_covid.gif"  alt="US video of a COVID-19 patient" width="100" height="172">  |  <img src="figure/6_butterfly_covid_cropped.gif" alt="cropped video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_cropped_convex_frame0.jpg" alt="first frame extracted from the video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_prc_convex_main_mask.jpg" alt="first frame mask" width="100" height="100">  |  <img src="figure/6_butterfly_covid_cropped_convex_frame67.jpg" alt="frame with moving pointer extracted from the video" width="100" height="100">  |  <img src="figure/6_butterfly_covid_prc_convex_frame67_mask.jpg" alt="frame with moving pointer mask" width="100" height="100">


# Core COVIDx-US Team
1. National Research Council Canada
    * Ashkan Ebadi (ashkan.ebadi@nrc-cnrc.gc.ca)
    * Pengcheng Xi
    * Stephane Tremblay
2. Vision and Image Processing Research Group, University of Waterloo, Canada
    * Alexander Wong (alexander.wong@uwaterloo.ca)
    * Alexander MacLean
3. St. Mary’s Hospital, McGill University, Canada
    * Adrian Florea

# Requirements
To generate the __COVIDx-US dataset__:
* Python >=3.6
* Pandas >=1.1.3
* BeautifulSoup
* selenium >=3.141.0
* requests >=2.24.0
* vimeo-downloader >=0.2.4
* zipfile
* Jupyter

# How to Generate the COVIDx-US Dataset?
1. Use create_COVIDxUS.ipynb to extract the ultrasound videos from multiple sources and integrate them in the COVIDx-US dataset. 
    * __Note 1:__ Make sure to modify the file paths in the code to your own paths, if reuqired.
	* __Note 2:__ See [data dictionary](https://github.com/nrc-cnrc/COVID-US/blob/main/utils/Data%20Dictionary.xlsx) file for details about variables/features in the metadata files. 

# COVIDx-US Data Distribution
Ultrasound __videos__ distribution per label and probe type

Class | Convex | Linear | Total
--- | --- | --- | ---
__COVID-19__ | 63 | 8 | `71`
__Pneumonia__ | 40 | 9 | `49`
__Normal__ | 19 | 9 | `28`
__Other__ | 68 | 26 | `94`



Ultrasound __videos__ distribution per label and data source

Class | ButterflyNetwork | PocusAtlas | GrepMed | LITFL | Radiopaedia | CoreUltrasound | Papers | UF | Clarius | Total
--- | --- | --- | --- | ---  | --- | --- | --- | --- | --- | ---
__COVID-19__ | 33 | 18 | 8 | 0 | 0 | 1 | 7 | 0 | 4 | `71`
__Pneumonia__ | 0 | 9 | 9 | 19 | 1 | 3 | 0 | 1 | 7 | `49`
__Normal__ | 2 | 5 | 3 | 3 | 1 | 1 | 4 | 6 | 3 | `28`
__Other__ | 0 | 0 | 0 | 41 | 3 | 13 | 11 | 17 | 9 | `94`


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

# Related works
* COVID-19 lung ultrasound [dataset](https://github.com/jannisborn/covid19_ultrasound/tree/master/data), link to the [paper](https://www.mdpi.com/2076-3417/11/2/672/html).

# COVID-Net team's other datasets for COVID-19 detection
* __[COVIDx](https://github.com/lindawangg/COVID-Net/blob/master/docs/COVIDx.md)__: 16,352 chest x-ray images across 14,979 patients
* __[COVIDx-CT](https://www.kaggle.com/hgunraj/covidxct)__: 201,103 chest CT slices from 4,501 patients
