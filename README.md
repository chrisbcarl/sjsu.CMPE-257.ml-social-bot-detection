# sjsu.CMPE-257.ml-social-bot-detection
SJSU 2026F CMPE 257 - Scalable and Generalizable Social Bot Detection through Data Selection - implementation


# Setup
```bash
# request the data from the researchers
poetry install
jupyter notebook ./classifier.ipynb
```


# Paper
[Scalable and Generalizable Social Bot Detection through Data Selection](https://doi.org/10.1609/aaai.v34i01.5460)
- Kai-Cheng Yang
- Onur Varol
- Pik-Mai Hui
- Filippo Menczer


# Conclusions

- "No dataset can generalize well on other datasets."

    > CONFIRMED - `cresci-17` did not generalize well to `twibot-22`

- "Selection is a promising direction for dealing with noisy training data."

    > CONFIRMED - `cresci-17` could be data selected to improve generalizability.

    |Test                      |Features|AUC      |
    |---                       |---     |---      |
    |cresci-17 cross-validation|20      |0.998    |
    |cresci-17 cross-validation|16      |0.994    |
    |cresci-17 → TwiBot-22     |16      |**0.606**|


# Datasets
## cresci-17
- `Dr. Stefano Cresci <stefano.cresci@iit.cnr.it>`
    - [Dr. Stefano Cresci](https://stefanocresci.com/)
- [request/hosting](http://mib.projects.iit.cnr.it/dataset.html)
    - [data csv](https://afs.tools.iit.cnr.it/f/2e00752708/)
    - [data sql (MySQL)](https://afs.tools.iit.cnr.it/f/3d90027eb4/)

## TwiBot-22 / TwiBot-20
- `Shangbin Feng <shangbin@cs.washington.edu>`
    - [Shangbin Feng](https://bunsenfeng.github.io/)
- [google-group](https://groups.google.com/g/twibot_access)
    - [data json, TwiBot-22](https://drive.google.com/drive/u/1/folders/1YwiOUwtl8pCd2GD97Q_WEzwEUtSPoxFs)
    - [data json, TwiBot-20](https://drive.google.com/drive/u/1/folders/1YY_fFK-ZS0lFDvoLaijoCp0yQ1CnG33i)


# Authors
|Name             |Email                       |Github Username           |Contributions                               |
|---              |---                         |---                       |---                                         |
|Chris Carl       |<chris.carl@sjsu.edu>       |data acquisition, slides, secondary implementation|
|Jehu Zepeda-Silva|<jehu.zepeda-silva@sjsu.edu>|jehuzepeda-silva-rgb      |primary implementation                              |
