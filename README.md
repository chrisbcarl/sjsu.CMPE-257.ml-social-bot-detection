# sjsu.CMPE-257.ml-social-bot-detection
SJSU 2026F CMPE 257 - Scalable and Generalizable Social Bot Detection through Data Selection - implementation


# Setup
```powershell
poetry install
choco install mysql mysql.odbc msql-cli -y
```
- mysql and workbench
    https://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-community-8.0.46.0.msi
    https://cdn.mysql.com//Downloads/MySQLGUITools/mysql-workbench-26.10.0-winx64.msi


# Paper
[Scalable and Generalizable Social Bot Detection through Data Selection](https://doi.org/10.1609/aaai.v34i01.5460)
- Kai-Cheng Yang
- Onur Varol
- Pik-Mai Hui
- Filippo Menczer


# Datasets
## cresci-17
- `Dr. Stefano Cresci <stefano.cresci@iit.cnr.it>`
    - [Dr. Stefano Cresci](https://stefanocresci.com/)
- [request/hosting](http://mib.projects.iit.cnr.it/dataset.html)
    - [data sql (MySQL)](https://afs.tools.iit.cnr.it/f/3d90027eb4/)
    - [data csv](https://afs.tools.iit.cnr.it/f/2e00752708/)

## TwiBot-22 / TwiBot-20
- `Shangbin Feng <shangbin@cs.washington.edu>`
    - [Shangbin Feng](https://bunsenfeng.github.io/)
- [google-group](https://groups.google.com/g/twibot_access)
    - [data json, TwiBot-22](https://drive.google.com/drive/u/1/folders/1YwiOUwtl8pCd2GD97Q_WEzwEUtSPoxFs)
    - [data json, TwiBot-20](https://drive.google.com/drive/u/1/folders/1YY_fFK-ZS0lFDvoLaijoCp0yQ1CnG33i)


# Authors
|Name             |Email                       |Github Username           |Contributions                               |
|---              |---                         |---                       |---                                         |
|Chris Carl       |<chris.carl@sjsu.edu>       |chrisbcarl, chriscarl-sjsu|Project management, implementation attempt 1|
|Jehu Zepeda-Silva|<jehu.zepeda-silva@sjsu.edu>|jehuzepeda-silva-rgb      |ISA Definition                              |
