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
from .base import SabaAuthenticationMethod


class CertificateAuthentication(SabaAuthenticationMethod):
    def __init__(self, host, username, password, site=None, site_name=None):
        self.certificate = CertificateAuthentication.get_certificate(host,
                                                                     username,
                                                                     password,
                                                                     site,
                                                                     site_name)
    @staticmethod
    def get_certificate(host, username, password, site=None, site_name=None):
        headers = {
            'user': username,
            'password': password
        }
        if site is not None:
            headers['site'] = site
        if site_name is not None:
            headers['site_name'] = site_name
        url = 'https://{0}/v1/login'.format(host)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()['certificate']

    def add_headers(self, headers={}):
        headers['SabaCertificate'] = self.certificate
        return headers
