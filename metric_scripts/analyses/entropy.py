# The Topic Browser
# Copyright 2010-2011 Brigham Young University
#
# This file is part of the Topic Browser <http://nlp.cs.byu.edu/topic_browser>.
#
# The Topic Browser is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# The Topic Browser is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License
# for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with the Topic Browser.  If not, see <http://www.gnu.org/licenses/>.
#
# If you have inquiries regarding any further use of the Topic Browser, please
# contact the Copyright Licensing Office, Brigham Young University, 3760 HBLL,
# Provo, UT 84602, (801) 422-9339 or 422-3821, e-mail copyright@byu.edu.

from math import log
from topic_modeling.visualize.models import AnalysisMetric, AnalysisMetricValue

def add_metric(analysis):
    metric, _ = AnalysisMetric.objects.get_or_create(name="Topic Entropy")
    
    # Get normalized topic counts
    counts = [topic.total_count for topic in analysis.topic_set.all()]
    total = float(sum(counts))
    
    entropy = 0.0
    for count in counts:
        prob = float(count) / total
        entropy -= prob * log(prob) / log(2)
    
    AnalysisMetricValue.objects.create(metric=metric, analysis=analysis, value=entropy)

def metric_names_generated(_analysis):
    return ["Topic Entropy"]