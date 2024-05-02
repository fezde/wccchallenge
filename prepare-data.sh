##############################################################################
# Install data for ntlk
#
# Please make sure you understand the copyrights for this data as described
# in the section "NTLK" of readme.md
##############################################################################
python -m nltk.downloader popular

##############################################################################
# Get all the english text files from Universität Leipzig
#
# Please make sure you have read and understood the copyright notice for this
# data mentioned in section "Text Corpus of the Universität Leipzig" of
# the readme.md file
##############################################################################
cd ./data
curl --remote-name-all https://downloads.wortschatz-leipzig.de/corpora/eng_news_[2005-2010]_1M.tar.gz
curl --remote-name-all https://downloads.wortschatz-leipzig.de/corpora/eng_news_[2013-2020]_1M.tar.gz
curl --remote-name-all https://downloads.wortschatz-leipzig.de/corpora/eng_news_2023_1M.tar.gz
for f in *.tar.gz; do tar -xvf "$f"; done
cd ..

##############################################################################
# Generate word frequencies
##############################################################################
python ./prepare/create_word_frequency_table.py
