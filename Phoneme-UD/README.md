# Phonemicised Universal Dependencies

Raw Test Universal Dependencies – train, test, dev from  Universal Dependencies 2.15 (Zeman et al., 2024 [https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-5787]). 

We use a corpus phonemicizer – G2P+ (https://github.com/codebyzeb/g2p-plus) – to convert raw UD into phonemic representations. 


| Language      | ISO Code | Epitran Mode(s)                          | Notes                                 |
|---------------|----------|------------------------------------------|----------------------------------------|
| Amharic       | am       | amh-Ethi, amh-Ethi-pp, amh-Ethi-red      | Naive, Precise phonemic, Reduced modes |
| Azerbaijani   | az       | aze-Cyrl, aze-Latn                       | —                                      |
| Catalan       | ca       | cat-Latn                                 | —                                      |
| German        | de       | deu-Latn, deu-Latn-np                    | Naive phonemic mode available          |
| English       | en       | eng-Latn                                 | —                                      |
| Spanish       | es       | spa-Latn                                 | —                                      |
| Farsi         | fa       | fas-Arab                                 | No short vowels                        |
| French        | fr       | fra-Latn, fra-Latn-np                    | Provisional, Naive phonemic            |
| Hindi         | hi       | hin-Deva                                 | —                                      |
| Hungarian     | hu       | hun-Latn                                 | —                                      |
| Italian       | it       | ita-Latn                                 | —                                      |
| Marathi       | mr       | mar-Deva                                 | —                                      |
| Polish        | pl       | pol-Latn                                 | —                                      |
| Portuguese    | pt       | por-Latn                                 | —                                      |
| Russian       | ru       | rus-Cyrl                                 | Provisional                            |
| Swedish       | sv       | swe-Latn                                 | —                                      |
| Tamil         | ta       | tam-Taml                                 | —                                      |
| Telugu        | te       | tel-Telu                                 | —                                      |
| Thai          | th       | tha-Thai                                 | —                                      |
| Tagalog       | tl       | tgl-Latn                                 | —                                      |
| Turkish       | tr       | tur-Latn, tur-Latn-bab                   | “Following Babel” mode available       |
| Uyghur        | ug       | uig-Arab                                 | —                                      |
| Ukrainian     | uk       | ukr-Cyrl                                 | Provisional                            |
| Vietnamese    | vi       | vie-Latn                                 | —                                      |
| Chinese       | zh       | cmn-Hans, cmn-Hant                       | Simplified and Traditional available.   |


| Language      | ISO Code | Phonemizer Mode(s)                          | Notes                                 |
|---------------|----------|------------------------------------------|----------------------------------------|
| Afrikaans       | af       |      | Naive, Precise phonemic, Reduced modes |


## Epitran 

| Code | Language (Script) | Notes |
|------|-----------------|-------|
| aar-Latn | Afar | |
| amh-Ethi | Amharic | Naive mode |
| amh-Ethi-pp | Amharic | Precise phonemic mode |
| amh-Ethi-red | Amharic | Reduced inventory mode |
| ara-Arab | Arabic | No short vowels |
| aze-Cyrl | Azerbaijani (Cyrillic) | |
| aze-Latn | Azerbaijani (Latin) | |
| ben-Beng | Bengali | |
| cat-Latn | Catalan | |
| ceb-Latn | Cebuano | |
| cmn-Hans | Chinese (Simplified) | |
| cmn-Hant | Chinese (Traditional) | |
| ckb-Arab | Sorani | Provisional |
| deu-Latn | German | |
| deu-Latn-np | German | Naive phonemic |
| eng-Latn | English | |
| fas-Arab | Farsi | No short vowels |
| fra-Latn | French | Provisional |
| fra-Latn-np | French | Naive phonemic |
| hat-Latn-bab | Haitian | Following Babel |
| hau-Latn | Hausa | |
| hin-Deva | Hindi | |
| hun-Latn | Hungarian | |
| ilo-Latn | Ilocano | |
| ind-Latn | Indonesian | |
| ita-Latn | Italian | |
| jav-Latn | Javanese | |
| kaz-Cyrl-bab | Kazakh (Cyrillic) | Following Babel |
| kaz-Cyrl | Kazakh (Cyrillic) | |
| kaz-Latn | Kazakh (Latin) | |
| khm-Khmr | Khmer | Provisional |
| kin-Latn | Kinyarwanda | |
| kir-Arab | Kyrgyz (Perso-Arabic) | |
| kir-Cyrl | Kyrgyz (Cyrillic) | |
| kir-Latn | Kyrgyz (Latin) | |
| kmr-Latn | Kurmanji | |
| lao-Laoo | Lao | Provisional |
| mar-Deva | Marathi | |
| mon-Cyrl-bab | Mongolian | Following Babel |
| mlt-Latn | Maltese | |
| msa-Latn | Malay | |
| mya-Mymr | Burmese | Provisional |
| nld-Latn | Dutch | |
| nya-Latn | Chichewa | |
| orm-Latn | Oromo | |
| pan-Guru | Punjabi | |
| pol-Latn | Polish | |
| por-Latn | Portuguese | |
| rus-Cyrl | Russian | Provisional |
| sna-Latn | Shona | |
| som-Latn | Somali | |
| spa-Latn | Spanish | |
| swa-Latn | Swahili | |
| swe-Latn | Swedish | |
| tam-Taml | Tamil | |
| tel-Telu | Telugu | |
| tgk-Cyrl | Tajik | |
| tgl-Latn | Tagalog | |
| tha-Thai | Thai | |
| tir-Ethi | Tigrinya | Naive |
| tir-Ethi-pp | Tigrinya | Precise phonemic mode |
| tir-Ethi-red | Tigrinya | Reduced inventory mode |
| tuk-Cyrl | Turkmen (Cyrillic) | |
| tuk-Latn | Turkmen (Latin) | |
| tur-Latn-bab | Turkish | Following Babel |
| tur-Latn | Turkish | |
| uig-Arab | Uyghur | |
| ukr-Cyrl | Ukrainian | Provisional |
| urd-Arab | Urdu | No short vowels |
| uzb-Cyrl | Uzbek (Cyrillic) | |
| uzb-Latn | Uzbek (Latin) | |
| vie-Latn | Vietnamese | |
| xho-Latn | Xhosa | |
| yor-Latn | Yoruba | |
| zha-Latn | Zhuang | |
| zul-Latn | Zulu | |

**Table 1: Language modes in Epitran**
