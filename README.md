Hello!

This is a project where I am attempting to Google Search on a Zoom Recording.

My first step was to attempt coreference resolution using neuralcoreference. Unfortunately, this didn't change any of the text, possibly because the transcript was not very accurate. I then tried wikifier and spaCy for NER. Both worked, although I believe spaCy's models worked a little better. You can find the important functions in helpers.py. The rest of the code was tested in the jupyter notebook file.
