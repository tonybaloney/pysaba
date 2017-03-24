#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test licensing client base functionality
"""
from requests_staticmock import (BaseMockClass,
                                 mock_session_with_class)
from requests_staticmock.responses import StaticResponseFactory
import json
import pytest
from six import b
