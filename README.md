## README.md and README_original.md

This project is a fork of an update of the original Feng-Hirst RST parser repo. The original README.md is included as README_original.md. It is recommended to install this project as a Python package and use it that way. This should simplifiy usage significantly and make it more accessible.
This README.md will focus on the current version and does not include instructions for how to run the original version.


## DEVELOPERS
* Original author: [Vanessa Wei Feng](mailto:weifeng@cs.toronto.edu), Department of Computer Science, University of Toronto, Canada  
* [Arne Neumann](mailto:github+spam.or.ham@arne.cl) updated it to use nltk 3.4 on [this github repo](https://github.com/arne-cl/feng-hirst-rst-parser), and created a Dockerfile.  
* [Zining Zhu](mailto:zining@cs.toronto.edu) updated the scripts to use Python 3.
* Thomas Huber, Chair of Data Science and Natural Language Processing, University of St. Gallen, updated the scripts further and added the `networkx` functionality.


## REFERENCES
* Vanessa Wei Feng and Graeme Hirst, 2014. Two-pass Discourse Segmentation with Pairing and Global Features. arXiv:1407.8215v1. http://arxiv.org/abs/1407.8215
* Vanessa Wei Feng and Graeme Hirst, 2014. A Linear-Time Bottom-Up Discourse Parser with Constraints and Post-Editing. In Proceedings of the 52th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (ACL-2014), Baltimore, USA. http://aclweb.org/anthology/P14-1048


## GENERAL INFOMRATION
* This RST-style discourse parser produces discourse tree structure on full-text level, given a raw text. No prior sentence splitting or any sort of preprocessing is expected. The program runs on Linux systems.
* The overall software work flow is similar to the one described in the paper by Feng and Hirst (ACL 2014). They removed the post-editing component from the workflow, as well as the set of entity-based transaction features from our feature set. Moreover, both structure and relation classification models are implemented using CRFSuite.


## SOFTWARE USAGE
See [`example.py`](feng_hirst_parser/example.py) for a very simple example.


## BUGS AND COMMENTS
If you encounter and bugs using the program, please create an Issue on the [GitHub repo](https://github.com/ThHuberSG/feng-hirst-rst-parser).