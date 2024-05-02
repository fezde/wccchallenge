# FEZ's #wccChallenge tools

This repository contains files that I use to prepare data for my sketches that I submit to Sableraph's great [weekly creative coding challenge on openprocessing.org](https://openprocessing.org/curation/78544).

## Getting started

First thing you need to do: Get all the data:

```bash
pip install -r requirements.txt
./prepare-data.sh
```

This will put all required data into the data directory, all follow-up and sketch specific scripts will rely on this data to exist. So do not miss this step. The other scripts will most possibly not check whether the data directory is set up correctly or not.

Now you can run the according scipts. Each of them will contain some more details and a link to the sketch(es) their output is used in.

## Shoutouts

This project is part of my works that I submit to the #wccchallenge held on openprocessing.org. My shoutouts go to:

* Raphaël for creating and running the challenge 
* the creators and conrtibutors of p5js and openprocessing - without them, creativity would be different today
* all participants of the challenge

## Copyrights

This section contains copyright notices of data that is used throughout this project. If a script uses special data that is not yet mentioned in this section, it will be mentioned in the according script. So always make sure you understand all required copyrights

### Text Corpus of the Universität Leipzig

The base texts of a lot of scripts in this project are taken from the corpus provided by the Universität Leipzig. So make sure you understand their copyright below.

> Any data and applications provided by Projekt Deutscher Wortschatz are subject to copyright. Permission for use is granted free of charge solely for non-commercial personal and scientific purposes licensed under the Creative Commons License CC BY-NC. Any use that exceeds the means of query provided by the WWW-Interface, any automated queries (except using our RESTful Webservices) and any commercial use of the data obtained is forbidden without explicit written permission by the copyright owner.
> All corpora provided for download are licensed under CC BY. If you are interested in larger data sets, please contact us.
>
> Please include the following copyright notice:
> © 2024 Universität Leipzig / Sächsische Akademie der Wissenschaften / InfAI.

### NTLK

As some of the scripts make heavy usage of the ntlk package, please see their copyright statement below.

> NLTK is open source software. The source code is distributed under the terms of the [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). The documentation is distributed under the terms of the [Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 United States license](http://creativecommons.org/licenses/by-nc-nd/3.0/us/). The corpora are distributed under various licenses, as documented in their respective README files.
