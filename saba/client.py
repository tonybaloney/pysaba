# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
from .exceptions import SabaApiException


class SabaClient(object):
    def __init__(self, host, auth, version='v1'):
        self.host = host
        self.base_url = 'https://{0}/{1}'.format(host, version)
        self.auth = auth
        self.session = requests.Session()
        self.session.headers.update(self.auth.add_headers({}))

        self._courses = None

    # Lazy properties

    @property
    def courses(self):
        if self._courses is None:
            from .apis.courses import CoursesClient
            self._courses = CoursesClient(self)
        return self._courses

    # HTTP Client methods

    def get(self, uri, params=None):
        try:
            result = self.session.get("{0}/{1}".format(self.base_url, uri),
                                      params=params)
            result.raise_for_status()
            return result.json()
        except requests.HTTPError as e:
            raise SabaApiException(e.response.text, uri)

    def post(self, uri, data=None):
        try:
            result = self.session.post("{0}/{1}".format(self.base_url, uri),
                                       json=data)
            result.raise_for_status()

            return result.json()
        except requests.HTTPError as e:
            raise SabaApiException(e.response.text)

    def put(self, uri, data=None):
        try:
            result = self.session.put("{0}/{1}".format(self.base_url, uri),
                                      json=data)
            result.raise_for_status()
        except requests.HTTPError as e:
            raise SabaApiException(e.response.text)

    def delete(self, uri):
        try:
            result = self.session.delete("{0}/{1}".format(self.base_url, uri))
            result.raise_for_status()
        except requests.HTTPError as e:
            raise SabaApiException(e.response.text)