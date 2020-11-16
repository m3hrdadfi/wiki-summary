# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TODO: Wiki Summary."""

from __future__ import absolute_import, division, print_function

import hashlib
import logging
import os

import datasets

# TODO: Add BibTeX citation
_CITATION = """\
@misc{Bert2BertFaWikiSummary,
  author = {Mehrdad Farahani},
  title = {Summarization using Bert2Bert model on WikiSummary dataset},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {https://github.com/m3hrdadfi/wiki-summary},
}
"""

# TODO: Add description of the dataset here
_DESCRIPTION = """\
Wiki Summary
The dataset extracted from Persian Wikipedia into the form of articles and summaries. The dataset cleaned into pairs of articles and highlights and reduced the articles' length and highlights' length to a maximum of 512 and 128, respectively.
Dataset Information
===================
Train	45,653	
Dev	    5,073
Test    5,637
"""

_DL_URLS = {
    # pylint: disable=line-too-long
    "wiki_summary": "https://drive.google.com/uc?id=19EVNUHzmzjDliShr6Pd1BnNx2k6_SVyg",
    "val_urls": "https://drive.google.com/uc?id=1NRqzz5y2EsdE6C702ShwX2Q4J1T5tyT3",
    "test_urls": "https://drive.google.com/uc?id=1RSqSKelNzHMjibmwQSR-yIN0yDbtk701",
    "train_urls": "https://drive.google.com/uc?id=1RospSAaplQ2axkaD1eUsrTfJs2N-HXqq",
    # pylint: enable=line-too-long
}

TEMPLATE_HIGHLIGHTS = "@highlight"
_HIGHLIGHTS = "highlights"
_ARTICLE = "article"

_SUPPORTED_VERSIONS = [
    datasets.Version("1.0.0", "First version of article and highlights from Wikipedia"),
]


class WikiSummaryConfig(datasets.BuilderConfig):
    """BuilderConfig for WikiSummary"""

    def __init__(self, **kwargs):
        """
        BuilderConfig for WikiSummary

        Args:
            **kwargs: keyword argument forwarded to super.
        """
        super(WikiSummaryConfig, self).__init__(**kwargs)


def _get_url_hashes(path):
    """Get hashes of urls in file."""
    urls = _read_text_file(path)

    def url_hash(u):
        h = hashlib.sha1()
        try:
            u = u.encode("utf-8")
        except UnicodeDecodeError:
            logging.error("Cannot hash url: %s", u)
        h.update(u)
        return h.hexdigest()

    return {url_hash(u): True for u in urls}


def _get_hash_from_path(p):
    """Extract hash from path."""
    basename = os.path.basename(p)
    return basename[0: basename.find(".story")]


def _find_files(dl_paths, publisher, url_dict):
    """Find files corresponding to urls."""
    if publisher == "wiki_summary":
        top_dir = os.path.join(dl_paths["wiki_summary"], "wiki_summary", "stories")
    else:
        logging.fatal("Unsupported publisher: %s", publisher)
    files = sorted(os.listdir(top_dir))

    ret_files = []
    for p in files:
        if _get_hash_from_path(p) in url_dict:
            ret_files.append(os.path.join(top_dir, p))
    return ret_files


def _subset_filenames(dl_paths, split):
    """Get filenames for a particular split."""
    assert isinstance(dl_paths, dict), dl_paths
    # Get filenames for a split.
    if split == datasets.Split.TRAIN:
        urls = _get_url_hashes(dl_paths["train_urls"])
    elif split == datasets.Split.VALIDATION:
        urls = _get_url_hashes(dl_paths["val_urls"])
    elif split == datasets.Split.TEST:
        urls = _get_url_hashes(dl_paths["test_urls"])
    else:
        logging.fatal("Unsupported split: %s", split)
    files = _find_files(dl_paths, "wiki_summary", urls)
    return files


DM_SINGLE_CLOSE_QUOTE = "\u2019"  # unicode
DM_DOUBLE_CLOSE_QUOTE = "\u201d"
# acceptable ways to end a sentence
END_TOKENS = [".", "!", "?", "...", "'", "`", '"', DM_SINGLE_CLOSE_QUOTE, DM_DOUBLE_CLOSE_QUOTE, ")"]


def _read_text_file(text_file):
    lines = []
    with open(text_file, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
    return lines


def _get_art_abs(story_file, tfds_version):
    """Get headline (highlights) and article from a story file path."""
    # Based on https://github.com/abisee/cnn-dailymail/blob/master/
    #     make_datafiles.py

    lines = _read_text_file(story_file)

    # The github code lowercase the text and we removed it in 3.0.0.

    # Put periods on the ends of lines that are missing them
    # (this is a problem in the dataset because many image captions don't end in
    # periods; consequently they end up in the body of the article as run-on
    # sentences)
    def fix_missing_period(line):
        """Adds a period to a line that is missing a period."""
        if TEMPLATE_HIGHLIGHTS in line:
            return line
        if not line:
            return line
        if line[-1] in END_TOKENS:
            return line
        return line + " ."

    lines = [fix_missing_period(line) for line in lines]

    # Separate out article and headline sentences
    article_lines = []
    highlights = []
    next_is_highlight = False
    for line in lines:
        if not line:
            continue  # empty line
        elif line.startswith(TEMPLATE_HIGHLIGHTS):
            next_is_highlight = True
        elif next_is_highlight:
            highlights.append(line)
        else:
            article_lines.append(line)

    # Make article into a single string
    article = " ".join(article_lines)

    if tfds_version >= "2.0.0":
        headline = "\n".join(highlights)
    else:
        headline = " ".join(highlights)

    return article, headline


class WikiSummary(datasets.GeneratorBasedBuilder):
    """WikiSummary non-anonymized wiki-summary dataset."""

    BUILDER_CONFIGS = [
        WikiSummaryConfig(name=str(version), description="Plain text", version=version)
        for version in _SUPPORTED_VERSIONS
    ]

    def _info(self):
        # Should return a datasets.DatasetInfo object
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    _ARTICLE: datasets.Value("string"),
                    _HIGHLIGHTS: datasets.Value("string"),
                    "id": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
            homepage="https://github.com/m3hrdadfi/wiki-summary",
            citation=_CITATION,
        )

    def _vocab_text_gen(self, paths):
        for _, ex in self._generate_examples(paths):
            yield " ".join([ex[_ARTICLE], ex[_HIGHLIGHTS]])

    def _split_generators(self, dl_manager):
        dl_paths = dl_manager.download_and_extract(_DL_URLS)
        train_files = _subset_filenames(dl_paths, datasets.Split.TRAIN)
        # Generate shared vocabulary

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"files": train_files}),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={"files": _subset_filenames(dl_paths, datasets.Split.VALIDATION)},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST, gen_kwargs={"files": _subset_filenames(dl_paths, datasets.Split.TEST)}
            ),
        ]

    def _generate_examples(self, files):
        for p in files:
            article, highlights = _get_art_abs(p, self.config.version)
            if not article or not highlights:
                continue
            fname = os.path.basename(p)
            yield fname, {
                _ARTICLE: article,
                _HIGHLIGHTS: highlights,
                "id": _get_hash_from_path(fname),
            }
